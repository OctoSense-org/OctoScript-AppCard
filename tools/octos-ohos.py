"""Normal-generation HarmonyOS deploy/launch. Invoked only by Studio RunItem."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import shlex
import subprocess
import time
import zipfile


def main():
    root = Path(os.environ['OCTOS_OHOS_ROOT'])
    request_path = Path(os.environ['OCTOS_OHOS_REQUEST'])
    request = json.loads(request_path.read_text()) if request_path.exists() else {}
    build = os.environ['STUDIO_BUILD']
    evidence = Path(request.get('evidence_dir', '/tmp/octos-ohos-generation'))
    evidence.mkdir(parents=True, exist_ok=True)
    project = root / 'app/target/makepad-open-harmony/octos_app'
    tool = root / 'makepad/target/release/cargo-makepad'
    hdc = os.environ['HDC']
    device = os.environ.get('OCTOS_OHOS_DEVICE') or request.get('device')
    if not device:
        output = subprocess.check_output([hdc, 'list', 'targets'], text=True)
        if 'Connect server failed' in output or '[Fail]' in output:
            raise SystemExit('HDC device discovery failed; reconnect the local HDC server')
        targets = [t.strip() for t in output.splitlines() if t.strip() and '[Empty]' not in t]
        if len(targets) != 1:
            raise SystemExit('Set OCTOS_OHOS_DEVICE when there is not exactly one connected device')
        device = targets[0]

    def device_run(*args, quiet=False):
        retry_read = args[:2] == ('fport', 'ls')
        if args[0] == 'shell':
            args = ('shell', shlex.join(args[1:]))
        for attempt in range(3 if retry_read else 1):
            p = subprocess.run([hdc, '-t', device, *args], capture_output=True, text=True)
            output = p.stdout + p.stderr
            if 'Connect server failed' not in output or not retry_read or attempt == 2:
                break
            time.sleep(1)
        if p.returncode or any(s in output for s in (
                '[Fail]', 'Permission denied', 'error: failed', 'Connect server failed')):
            # Arguments can contain private provisioning; never include them in an error.
            raise RuntimeError('HDC operation failed; inspect the device locally')
        if not quiet:
            print(output.strip(), flush=True)
        return output

    def build_app(command):
        log = evidence / f'build-{build}-{command}.log'
        with log.open('w') as out:
            p = subprocess.run([str(tool), 'ohos', '--deveco-home=' + os.environ['DEVECO_HOME'],
                                command, '-p', 'octos-app', '--release'],
                               cwd=root / 'app', stdout=out, stderr=subprocess.STDOUT)
        if p.returncode:
            raise SystemExit(f'Release build failed; private build log: {log}')

    if not request.get('skip_build', False):
        old_hap = project / 'entry/build/default/outputs/default/makepad-default-signed.hap'
        if old_hap.exists():
            backup = evidence / 'previous-signed.hap'
            if not backup.exists():
                shutil.copy2(old_hap, backup)
        if not (project / 'build-profile.json5').exists():
            build_app('deveco')
        profile_path = project / 'build-profile.json5'
        # Generated profiles contain trailing commas. Preserve quoted strings,
        # including URL and signing material, while removing those commas.
        raw_profile = profile_path.read_text()
        tokens = re.compile(r'"(?:\\.|[^"\\])*"|,\s*(?=[}\]])')
        profile = json.loads(tokens.sub(lambda m: '' if m.group().startswith(',') else m.group(), raw_profile))
        signing = Path(os.environ.get('OCTOS_OHOS_SIGNING_CONFIG',
                                      str(Path.home() / 'ohos-sdk/signing/agc-signingconfigs.json5')))
        if signing.exists():
            profile['app']['signingConfigs'] = json.loads(signing.read_text())
            profile['app']['products'][0]['signingConfig'] = 'default'
            profile_path.write_text(json.dumps(profile, indent=2))
        if not profile['app'].get('signingConfigs'):
            raise SystemExit('A local device signing configuration is required')
        template = root / 'makepad/tools/open_harmony/deveco/entry/src/main'
        for name in ('ets', 'cpp/types'):
            shutil.copytree(template / name, project / 'entry/src/main' / name, dirs_exist_ok=True)
        shutil.copy2(template / 'module.json5', project / 'entry/src/main/module.json5')
        # The core is linked into libmakepad on OHOS. Retire the earlier
        # executable bundle: HarmonyOS cannot exec it from the app sandbox.
        (project / 'entry/libs/arm64-v8a/liboctos.so').unlink(missing_ok=True)
        build_app('build')
        hap = project / 'entry/build/default/outputs/default/makepad-default-signed.hap'
        with zipfile.ZipFile(hap) as archive:
            if json.loads(archive.read('module.json'))['app'].get('debug', False):
                raise SystemExit('Expected a release package')
            native = archive.read('libs/arm64-v8a/libmakepad.so')
        device_run('install', '-r', str(hap))
        metadata = {
            'core_revision': subprocess.check_output(['git', '-C', str(root / 'octos'), 'rev-parse', 'HEAD'], text=True).strip(),
            'native_sha256': hashlib.sha256(native).hexdigest(),
            'core_transport': 'in-process OUP',
            'hap_sha256': hashlib.sha256(hap.read_bytes()).hexdigest(),
            'release': True,
        }
        (evidence / 'installed-build.json').write_text(json.dumps(metadata, indent=2) + '\n')
    port = str(request.get('studio_port', 8002))
    if not request.get('standalone', False):
        forwards = device_run('fport', 'ls', quiet=True)
        if not any(device in line and line.count('tcp:' + port) == 2 and '[Reverse]' in line for line in forwards.splitlines()):
            device_run('rport', 'tcp:' + port, 'tcp:' + port)
    device_run('shell', 'power-shell', 'wakeup', quiet=True)
    device_run('shell', 'aa', 'force-stop', 'dev.makepad.octos_app', quiet=True)
    args = ['shell', 'aa', 'start', '-a', 'EntryAbility', '-b', 'dev.makepad.octos_app']
    if request.get('reapprove_cards'):
        args.extend(['--ps', 'makepad.REAPPROVE_CARDS', build])
    if not request.get('standalone', False):
        args.extend(['--ps', 'makepad.STUDIO_HOST', '127.0.0.1:' + port,
                     '--ps', 'makepad.STUDIO_BUILD', build, '--ps', 'makepad.STUDIO_CRATE', 'octos-app'])
    if request.get('prompt'):
        args.extend(['--ps', 'makepad.AUTO_PROMPT', request['prompt']])
    # Optional local onboarding data uses the existing app provisioning path.
    # It is loaded here so no key is written into the repository, HAP or logs.
    if request.get('provision_file'):
        private = json.loads(Path(request['provision_file']).read_text())
        args.extend(['--ps', 'makepad.PROVISION_CONFIG', json.dumps(private, separators=(',', ':'))])
    device_run(*args, quiet=True)
    print(f'Normal generation launched; Studio build {build}', flush=True)
    pid = device_run('shell', 'pidof', 'dev.makepad.octos_app', quiet=True).strip()
    if not pid.isdecimal():
        raise SystemExit('The app did not start')
    # Raw logs are local/private. Only credential-free timing rows reach Studio.
    with (evidence / f'device-{build}.log').open('w') as log:
        process = subprocess.Popen([hdc, '-t', device, 'shell', 'hilog', '-P', pid],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        try:
            for line in process.stdout:
                log.write(line)
                log.flush()
                if 'generation-metric ' in line:
                    print(line.strip(), flush=True)
        finally:
            process.terminate()


if __name__ == '__main__':
    main()
