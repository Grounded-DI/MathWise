import itertools,random,json,sys
from pathlib import Path
from fractions import Fraction

def greedy(A,mode):
 n=len(A);R=[row[:] for row in A];terms=[]
 while any(R[0]):
  if mode=='permutations':P=next(P for P in itertools.permutations(range(n)) if all(R[i][P[i]]>0 for i in range(n)))
  else:
   def search(prefix,used):
    i=len(prefix)
    if i==n:return tuple(prefix)
    for j in range(n):
     if R[i][j]>0 and j not in used:
      x=search(prefix+[j],used|{j})
      if x is not None:return x
   P=search([],set())
  t=min(R[i][P[i]] for i in range(n));terms.append({'mass':t,'permutation':P})
  for i in range(n):R[i][P[i]]-=t
  mass=sum(R[0]);assert all(sum(row)==mass for row in R) and all(sum(R[i][j] for i in range(n))==mass for j in range(n))
 assert all(x==0 for row in R for x in row)
 return terms
def check_reconstruction(A,terms,D):
 n=len(A)
 assert sum(t['mass'] for t in terms)==D and all(t['mass']>0 for t in terms)
 for i in range(n):
  for j in range(n):assert sum(Fraction(t['mass'],D)*(t['permutation'][i]==j) for t in terms)==Fraction(A[i][j],D)

out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);gen=random.Random(20261116);attempts=[];witness=None
for n,m,weights in [(4,4,[1,2,4,8]),(5,3,[1,2,4]),(5,3,[1,3,9]),(5,4,[1,2,4,8]),(6,3,[1,4,8])]:
 perms=list(itertools.permutations(range(n)));tested=0
 for case in range(10000):
  selected=[]
  for _ in range(m):
   choices=[P for P in perms if all(P[i]!=Q[i] for Q in selected for i in range(n))]
   if not choices:break
   selected.append(gen.choice(choices))
  if len(selected)<m:continue
  D=sum(weights);A=[[sum(w*(P[i]==j) for w,P in zip(weights,selected)) for j in range(n)] for i in range(n)]
  t=greedy(A,'permutations');tested+=1
  attempts.append({'n':n,'m':m,'weights':weights,'case':case,'G':len(t)})
  if len(t)>2*m:
   short=[{'mass':w,'permutation':P} for w,P in zip(weights,selected)]
   independent=greedy(A,'backtracking');assert independent==t
   check_reconstruction(A,t,D);check_reconstruction(A,short,D)
   row_supports=[sum(x>0 for x in row) for row in A];assert all(x==m for x in row_supports)
   witness={'n':n,'denominator':D,'integer_matrix':A,'greedy_terms':t,'short_decomposition':short,'G':len(t),'OPT':m,'row_support_counts':row_supports,'ratio':str(Fraction(len(t),m)),'search_case':case,'seed':20261116,'independent_greedy_agreement':True}
   break
 if witness:break
(out/'search_attempts.json').write_text(json.dumps(attempts,separators=(',',':'))+'\n')
if witness:(out/'counterexample.json').write_text(json.dumps(witness,indent=2)+'\n')
r={'classification':'COUNTEREXAMPLE FOUND' if witness else 'UNRESOLVED','search_inputs_checked':len(attempts),'counterexample':witness,'scope':'Structured seeded search, not exhaustive over matrices; two greedy implementations checked on witness; exact row-support bound and shorter decomposition certify OPT if found.','formal_verification':False,'external_review':False,'novelty_claim':False}
(out/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
