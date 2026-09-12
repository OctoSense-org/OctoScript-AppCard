"""Bounded recovery from blank Studio readbacks using committed checkpoints.

Every attempt delegates UI startup to the normal Studio RunItem renderer. A
failed structural/semantic mapping is never retryable as a graphics transport
error, and no failed screenshot receives an acceptance receipt.
"""
import argparse,json,signal,subprocess,sys,time,uuid
from pathlib import Path
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))
from core import kitconf

TRANSIENT=('empty native frame after three readbacks','Studio frame did not settle at')


def validate_sources(kit):
    if kit.get('input_format')!='l0-kit':return True
    from core.promote_l0 import PACKS
    out=kit['splash_makepad_dir'];audit=out/'capture-preflight.json'
    audit.unlink(missing_ok=True)
    command=['cargo','run','--release','-q','-p','splash-makepad','--example','kit_audit','--',
             str(kit['cards_dir']),str(kitconf.HERE/kit['source_designs_dir']),str(PACKS.parent),str(audit)]
    result=subprocess.run(command,cwd=kitconf.HERE.parents[1]/'splash-makepad',capture_output=True,text=True)
    (out/'capture-preflight.log').write_text(result.stdout+result.stderr)
    rows={r['screen']:r for r in json.loads(audit.read_text()).get('screens',[])} if audit.exists() else {}
    return result.returncode==0 and all(rows.get(name,{}).get('pass') for name in kit['screens'])


def attempt(kit,log):
    command=[sys.executable,str(Path(__file__).resolve().parents[1]/'core'/'render_splash_makepad.py'),'--kit',kit['name']]
    with log.open('w') as output,subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True) as process:
        try:
            for line in process.stdout:output.write(line);output.flush();print(line,end='',flush=True)
            return process.wait()
        except KeyboardInterrupt:
            process.send_signal(signal.SIGINT)
            try:process.wait(timeout=15)
            except subprocess.TimeoutExpired:process.kill();process.wait()
            raise


def run(kit,attempts=3,runner=attempt,validate=validate_sources):
    if not 1<=attempts<=3:raise ValueError('capture attempts must be between one and three')
    out=kit['splash_makepad_dir'];logs=out/'capture-attempts';logs.mkdir(parents=True,exist_ok=True)
    receipt={'kit':kit['name'],'status':'running','attempts':[]};path=out/'capture-recovery.json'
    def save():
        tmp=path.with_suffix('.pending.json');tmp.write_text(json.dumps(receipt,indent=2)+'\n');tmp.replace(path)
    save()
    try:
        if not validate(kit):
            receipt.update(status='failed',error='L0/source tree mismatch; repair or repromote before Studio capture')
            save();return False
        for index in range(attempts):
            log=logs/f'{time.time_ns()}-{uuid.uuid4().hex[:8]}.log';code=runner(kit,log)
            output=log.read_text();transient=bool(code and any(reason in output for reason in TRANSIENT))
            receipt['attempts'].append({'log':str(log),'returncode':code,'retryable_readback':transient})
            save()
            if code==0:receipt['status']='passed';save();return True
            if not transient:break
            print('Restarting Studio RunItem and resuming hash-verified capture checkpoints.',flush=True)
        receipt['status']='failed';save();return False
    except KeyboardInterrupt:
        receipt['status']='interrupted';save();raise
    except (OSError,ValueError,KeyError) as error:
        receipt.update(status='failed',error=str(error));save();return False


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--kit',required=True);p.add_argument('--attempts',type=int,default=3)
    a=p.parse_args();raise SystemExit(0 if run(kitconf.load(a.kit),a.attempts) else 1)
