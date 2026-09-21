#!/bin/sh
# Inspect a HarmonyOS App Pack or HAP: identity, manifest, permissions, signature,
# provisioning profile. Everything AppGallery checks before it will parse a pack.
set -eu
PKG=$1
DEVECO=/Applications/DevEco-Studio.app/Contents
export JAVA_HOME=$DEVECO/jbr/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH
T=$DEVECO/sdk/default/openharmony/toolchains/lib/hap-sign-tool.jar
W=$(mktemp -d)
trap 'rm -rf "$W"' EXIT

echo "== file =="
ls -la "$PKG" | awk '{print $5, "bytes"}'
file -b "$PKG"
shasum -a 256 "$PKG" | awk '{print "sha256", $1}'

cd "$W" && unzip -q "$PKG"
HAP=$(ls *.hap 2>/dev/null | head -1)
[ -n "$HAP" ] || HAP=$PKG

echo
echo "== identity =="
unzip -p "$HAP" module.json | python3 -c "
import sys, json
a = json.load(sys.stdin)['app']
for k in ('bundleName','versionName','versionCode','vendor','minAPIVersion','targetAPIVersion','apiReleaseType','debug','buildMode','icon','label'):
    print(f'{k:16} {a.get(k)}')
"
echo
echo "== module and permissions =="
unzip -p "$HAP" module.json | python3 -c "
import sys, json
m = json.load(sys.stdin)['module']
print('module          ', m['name'], '/', m['type'])
print('devices         ', m.get('deviceTypes'))
print('installationFree', m.get('installationFree'))
for p in m.get('requestPermissions', []):
    print('permission      ', p['name'])
"
echo
echo "== signature =="
java -jar "$T" verify-app -inFile "$PKG" -outCertChain "$W/c.cer" -outProfile "$W/p.p7b" 2>&1 \
  | grep -E "Subject|Validity|Signature Algorithm|verify:" | sed 's/^.*INFO - //'
echo
echo "== provisioning profile =="
python3 - "$W/p.p7b" <<'PY'
import json, sys, pathlib
raw = pathlib.Path(sys.argv[1]).read_bytes()
i = raw.find(b'{"version-name"')
if i < 0: i = raw.find(b'{"')
d = 0
for j in range(i, len(raw)):
    c = raw[j:j+1]
    if c == b'{': d += 1
    elif c == b'}':
        d -= 1
        if d == 0: end = j+1; break
p = json.loads(raw[i:end].decode())
b = p.get('bundle-info', {})
print('type            ', p.get('type'), '  <- AppGallery needs "release"')
print('bundle          ', b.get('bundle-name'))
print('certificate     ', 'distribution' if 'distribution-certificate' in b else 'development')
print('apl             ', b.get('apl'))
print('acls            ', p.get('acls', {}).get('allowed-acls'))
print('devices         ', len(p.get('debug-info', {}).get('device-ids', [])))
import datetime
v = p.get('validity', {})
for k in ('not-before','not-after'):
    if v.get(k): print(f'{k:16}', datetime.datetime.utcfromtimestamp(v[k]).strftime('%Y-%m-%d %H:%M UTC'))
PY
