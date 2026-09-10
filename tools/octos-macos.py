"""Launch the native mobile-sized desktop app through a Studio release RunItem."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import urllib.request


def main():
    os.umask(0o077)
    root = Path(__file__).resolve().parents[1]
    request_path = Path(os.environ.get('OCTOS_MACOS_REQUEST', '/tmp/octos-macos-request.json'))
    request = json.loads(request_path.read_text()) if request_path.exists() else {}
    build = os.environ['STUDIO_BUILD']
    state = Path(request.get('state_dir', str(Path.home() / 'Library/Application Support/Octos One Mobile')))
    core = state / 'core'
    app_config = state / 'app'
    for directory in [core / 'profiles', core / 'workspace', app_config,
                      core / 'profiles/_main/data/skills', core / 'profiles/_main/data/inbox']:
        directory.mkdir(parents=True, exist_ok=True)
    endpoint = request.get('model_base_url', 'http://127.0.0.1:30881/v1').rstrip('/')
    model = request.get('model', 'qwen3.8-27b')
    with urllib.request.urlopen(endpoint + '/models', timeout=10) as response:
        models = json.load(response)
    if model not in {item['id'] for item in models['data']}:
        raise SystemExit('Requested inference model is unavailable')

    # This profile belongs only to the mobile desktop test app. The endpoint
    # is reached over a local tunnel; the placeholder key is not a credential.
    profile_path = core / 'profiles/_main.json'
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    profile = json.loads(profile_path.read_text()) if profile_path.exists() else {
        'id': '_main', 'name': 'Main', 'enabled': True,
        'created_at': now, 'updated_at': now,
        'config': {},
    }
    profile['updated_at'] = now
    config = profile.setdefault('config', {})
    config.setdefault('llm', {})['primary'] = {
        'family_id': 'openai', 'model_id': model,
        'route': {'base_url': endpoint, 'api_type': request.get('api_type', 'responses')},
    }
    config['llm']['fallbacks'] = []
    config.setdefault('env_vars', {})['OPENAI_API_KEY'] = 'local-inference-no-auth'
    profile_path.write_text(json.dumps(profile, indent=2) + '\n')
    core_config_path = core / 'config.json'
    core_config = json.loads(core_config_path.read_text()) if core_config_path.exists() else {}
    core_config.setdefault('memory', {})['max_inject_tokens'] = 40000
    core_config_path.write_text(json.dumps(core_config, indent=2) + '\n')

    env = os.environ.copy()
    env.update(OCTOS_APP_CONFIG_DIR=str(app_config), OCTOS_APP_CORE_DIR=str(core),
               OCTOS_APP_CORE_BIN=str(root / 'octos/target/release/octos'),
               OCTOS_USER_STORE_PATH=str(app_config / 'user.json'),
               MAKEPAD_WINDOW_SIZE=request.get('window_size', '440x841'),
               MAKEPAD_MOBILE_PREVIEW='1')
    if request.get('browser_capture_dir'):
        env['MAKEPAD_BROWSER_CAPTURE_DIR'] = request['browser_capture_dir']
    if request.get('native_clicks'):
        env['MAKEPAD_STUDIO_NATIVE_CLICKS'] = '1'
    if request.get('disable_reference_cache'):
        env['OCTOS_A2APP_DISABLE_REFERENCE_CACHE'] = '1'
    if request.get('reapprove_cards'):
        env['MAKEPAD_REAPPROVE_CARDS'] = build
    if request.get('prompt'):
        env['MAKEPAD_AUTO_PROMPT'] = request['prompt']
    else:
        env.pop('MAKEPAD_AUTO_PROMPT', None)
    if not request.get('skip_build', False):
        subprocess.run(['cargo', 'build', '-p', 'octos-app', '--bin', 'octos-app',
                        '--release', '--message-format=json'], cwd=root / 'app', env=env, check=True)
    if not Path(env['OCTOS_APP_CORE_BIN']).is_file():
        raise SystemExit('Build the current native Octos core before launching this RunItem')
    evidence = Path(request.get('evidence_dir', '/tmp/octos-macos-generation'))
    evidence.mkdir(parents=True, exist_ok=True)
    print('Launching native mobile-sized Octos with the dedicated inference model', flush=True)
    process = subprocess.Popen([str(root / 'app/target/release/octos-app'), '--message-format=json'],
                               cwd=root / 'app', env=env, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, text=True, bufsize=1)
    try:
        with (evidence / f'app-{build}.log').open('w') as output:
            for line in process.stdout:
                output.write(line)
                output.flush()
                print(line, end='', flush=True)
        raise SystemExit(process.wait())
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait(timeout=10)


if __name__ == '__main__':
    main()
