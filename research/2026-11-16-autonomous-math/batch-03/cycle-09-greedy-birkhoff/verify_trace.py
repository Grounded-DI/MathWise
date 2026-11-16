from pathlib import Path
import json,itertools
from datetime import datetime,timezone
p=Path(__file__).resolve().parent
w=json.loads((p/'checks/counterexample.json').read_text());R=[r[:] for r in w['integer_matrix']];trace=[]
for k,t in enumerate(w['greedy_terms'],1):
 P=tuple(t['permutation']);blockers=[]
 for Q in itertools.permutations(range(w['n'])):
  if Q==P:break
  zeros=[(i,Q[i]) for i in range(w['n']) if R[i][Q[i]]==0]
  assert zeros;blockers.append({'earlier_permutation':Q,'zero_positions':zeros})
 assert all(R[i][P[i]]>0 for i in range(w['n']))
 assert min(R[i][P[i]] for i in range(w['n']))==t['mass']
 before=[r[:] for r in R]
 for i in range(w['n']):R[i][P[i]]-=t['mass']
 trace.append({'step':k,'before':before,'chosen_permutation':P,'minimum_subtracted':t['mass'],'after':[r[:] for r in R],'earlier_permutation_blockers':blockers})
assert not any(x for row in R for x in row)
target=p/'checks/lexicographic_trace_certificate.json';encoded=json.dumps(trace,indent=2)+'\n'
if target.exists():assert target.read_text()==encoded
target.write_text(encoded)
print(json.dumps({'status':'PASS','steps_checked':len(trace),'all_earlier_permutations_blocked':True,'checked_at_utc':datetime.now(timezone.utc).isoformat()}))
