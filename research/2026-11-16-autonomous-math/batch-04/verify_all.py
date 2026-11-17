"""Replay the published finite certificates. Python3 standard library; assertions enabled."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile
if not __debug__:
 raise SystemExit('Assertions must be enabled; omit -O.')
b=Path(__file__).resolve().parent
entries={}
for line in (b/'SHA256SUMS.txt').read_text().splitlines():
 h,p=line.split('  ',1)
 assert p not in entries and not Path(p).is_absolute() and '..' not in Path(p).parts
 entries[p]=h
assert set(entries)=={str(p.relative_to(b)) for p in b.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt'}
for p,h in entries.items():assert hashlib.sha256((b/p).read_bytes()).hexdigest()==h,p
for d in sorted(b.glob('cycle-*')):
 with tempfile.TemporaryDirectory() as out:
  r=subprocess.run([sys.executable,str(d/'verify.py'),out],cwd=d,capture_output=True,text=True,check=True)
  actual=list(Path(out).glob('*.json'))
  assert {p.name for p in actual}=={p.name for p in (d/'results').glob('*.json')}
  for p in actual:assert json.loads(p.read_text())==json.loads((d/'results'/p.name).read_text()),p.name
 if (d/'verify_trace.py').exists():
  subprocess.run([sys.executable,str(d/'verify_trace.py')],cwd=d,check=True,capture_output=True,text=True)
 print(d.name+': PASS')
print('SHA-256 inventory and all publication result comparisons: PASS')
