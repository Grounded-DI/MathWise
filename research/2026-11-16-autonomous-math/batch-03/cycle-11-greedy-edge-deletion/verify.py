from pathlib import Path
import itertools,json,sys,math
from fractions import Fraction

def tree(n,E):
 p=list(range(n))
 def root(a):
  while p[a]!=a:a=p[a]
  return a
 for a,b in E:
  a,b=root(a),root(b)
  if a==b:return False
  p[a]=b
 return len(E)==n-1 and len({root(i) for i in range(n)})==1

def determinant(A):
 A=[[Fraction(v) for v in row] for row in A];d=Fraction(1)
 for k in range(len(A)):
  q=next((i for i in range(k,len(A)) if A[i][k]),None)
  if q is None:return 0
  if q!=k:A[k],A[q]=A[q],A[k];d=-d
  v=A[k][k];d*=v
  for i in range(k+1,len(A)):
   f=A[i][k]/v
   for j in range(k+1,len(A)):A[i][j]-=f*A[k][j]
 return int(d)
def tau(n,E):
 L=[[0]*n for _ in range(n)]
 for a,b in E:L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
 return determinant([r[:-1] for r in L[:-1]])
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);checked=0;masks=0;subsets=0;logs=[];w=None
for n in range(4,7):
 U=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(U)):
  masks+=1;E=[e for j,e in enumerate(U) if mask>>j&1];m=len(E)
  if m<n+1:continue
  T=[]
  for S in itertools.combinations(range(m),n-1):
   subsets+=1
   if tree(n,[E[i] for i in S]):T.append(sum(1<<i for i in S))
  if not T:continue
  checked+=1
  singles=[sum(not(t>>i&1) for t in T) for i in range(m)]
  pairs={(i,j):sum(not(t&((1<<i)|(1<<j))) for t in T) for i,j in itertools.combinations(range(m),2)}
  a=max(range(m),key=lambda i:singles[i]);b=max((i for i in range(m) if i!=a),key=lambda i:pairs[tuple(sorted((a,i)))])
  gv=pairs[tuple(sorted((a,b)))];op=max(pairs.values());logs.append([n,mask,len(T),a,b,gv,op])
  if gv<op:
   w={'n':n,'mask':mask,'edges':E,'tree_masks':T,'tree_count':len(T),'singles':singles,'pairs':[{'indices':[i,j],'remaining':v} for (i,j),v in pairs.items()],'greedy_indices':[a,b],'greedy_value':gv,'optimum':op,'optimal_pairs':[list(k) for k,v in pairs.items() if v==op]};break
 if w:break
assert w
E=w['edges'];n=w['n'];m=len(E)
assert tau(n,E)==w['tree_count']
for i,v in enumerate(w['singles']):assert tau(n,[e for j,e in enumerate(E) if j!=i])==v
for row in w['pairs']:assert tau(n,[e for j,e in enumerate(E) if j not in row['indices']])==row['remaining']
# Different tree enumeration: rooted parent assignments, no union-find.
parents_count=0
for parents in itertools.product(*[[j for j in range(n) if j!=i and tuple(sorted((i,j))) in E] for i in range(1,n)]):
 good=True
 for i in range(1,n):
  seen=set();v=i
  while v!=0:
   if v in seen:good=False;break
   seen.add(v);v=parents[v-1]
  if not good:break
 if good:parents_count+=1
assert parents_count==len(w['tree_masks'])
r={'classification':'COUNTEREXAMPLE FOUND','masks_visited':masks,'connected_eligible_graphs_checked':checked,'candidate_tree_subsets_examined':subsets,'determinants_checked':1+m+math.comb(m,2),'rooted_parent_tree_count':parents_count,'formal_verification':False,'external_review':False,'novelty_claim':False}
for name,obj in [('witness.json',w),('search_log.json',logs),('results.json',r)]: (out/name).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(r));print(json.dumps({k:v for k,v in w.items() if k!='tree_masks'}))
