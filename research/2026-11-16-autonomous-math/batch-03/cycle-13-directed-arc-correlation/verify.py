from itertools import product,combinations
from fractions import Fraction
from pathlib import Path
import json,sys

def valid(n,es):
 p=dict(es)
 if len(p)!=n-1 or 0 in p:return False
 for v in range(1,n):
  seen=set()
  while v:
   if v in seen or v not in p:return False
   seen.add(v);v=p[v]
 return True

def det(a):
 a=[[Fraction(x) for x in r] for r in a];d=Fraction(1)
 for k in range(len(a)):
  j=next((j for j in range(k,len(a)) if a[j][k]),None)
  if j is None:return 0
  if j!=k:a[j],a[k]=a[k],a[j];d=-d
  v=a[k][k];d*=v
  for j in range(k+1,len(a)):
   q=a[j][k]/v
   for h in range(k+1,len(a)):a[j][h]-=q*a[k][h]
 assert d.denominator==1
 return int(d)

def cofactor(n,arcs,forced):
 L=[[0]*n for _ in range(n)]
 for u,v in arcs:
  if u in forced and v!=forced[u]:continue
  L[u][u]+=1;L[u][v]-=1
 return det([row[1:] for row in L[1:]])

p=Path(sys.argv[1]);p.mkdir(exist_ok=True);rows=[];tot=0;parents=0;paircases=0
for n in range(5,11):
 arcs=sorted([(i,(i+1)%n) for i in range(n)]+[((i+1)%n,i) for i in range(n)])
 ts=[]
 for choices in product(*[[e for e in arcs if e[0]==v] for v in range(1,n)]):
  parents+=1
  if valid(n,choices):ts.append(tuple(sorted(choices)))
 # Different route: undirected subset enumeration, union-find, then orient by BFS distance.
 edges=sorted({tuple(sorted(e)) for e in arcs});us=[]
 for subset in combinations(edges,n-1):
  tot+=1;adj=[[] for _ in range(n)]
  for u,v in subset:adj[u].append(v);adj[v].append(u)
  seen={0};queue=[0];oriented=[]
  for v in queue:
   for u in adj[v]:
    if u not in seen:seen.add(u);queue.append(u);oriented.append((u,v))
  if len(seen)==n:us.append(tuple(sorted(oriented)))
 assert sorted(ts)==sorted(us) and len(ts)==n==cofactor(n,arcs,{})
 pairs=[]
 for i in range(1,n-1):
  for j in range(i+2,n-1):
   e=(i,i+1);f=(j,j+1);A=sum(e in t for t in ts);B=sum(f in t for t in ts);AB=sum(e in t and f in t for t in ts)
   ds=[cofactor(n,arcs,dict([e])),cofactor(n,arcs,dict([f])),cofactor(n,arcs,dict([e,f]))]
   assert [A,B,AB]==ds==[i,j,i]
   cov=Fraction(AB,n)-Fraction(A*B,n*n);assert cov==Fraction(i*(n-j),n*n)>0
   pairs.append({'e':e,'f':f,'counts':[n,A,B,AB],'covariance':str(cov)});paircases+=1
 rows.append({'n':n,'arcs':arcs,'trees':ts,'pair_checks':pairs})
result={'graphs':6,'n_bounds':[5,10],'parent_assignments':parents,'undirected_subsets':tot,'disjoint_nonroot_pair_cases':paircases,'determinants':6+3*paircases,'all_checks_pass':True,'witness':rows[0]['pair_checks'][0]}
(p/'inputs_certificates.json').write_text(json.dumps(rows,indent=2)+'\n');(p/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
