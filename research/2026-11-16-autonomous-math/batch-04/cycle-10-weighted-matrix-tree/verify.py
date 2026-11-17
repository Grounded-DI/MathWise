import itertools,json,sys,random,math
from fractions import Fraction
from pathlib import Path

def det(A):
 A=[[Fraction(x) for x in row] for row in A];n=len(A);ans=Fraction(1)
 for k in range(n):
  pivot=next((i for i in range(k,n) if A[i][k]),None)
  if pivot is None:return Fraction(0)
  if pivot!=k:A[k],A[pivot]=A[pivot],A[k];ans=-ans
  a=A[k][k];ans*=a
  for i in range(k+1,n):
   f=A[i][k]/a
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
 return ans
def leibniz(A):
 n=len(A);return sum((-1)**sum(P[i]>P[j] for i in range(n) for j in range(i+1,n))*math.prod(A[i][P[i]] for i in range(n)) for P in itertools.permutations(range(n)))
def is_tree(n,E):
 if len(E)!=n-1:return False
 parent=list(range(n))
 def root(a):
  while parent[a]!=a:a=parent[a]
  return a
 for a,b in E:
  a,b=root(a),root(b)
  if a==b:return False
  parent[a]=b
 return len({root(a) for a in range(n)})==1
def lap(n,E,W):
 L=[[0]*n for _ in range(n)]
 for (a,b),w in zip(E,W):L[a][a]+=w;L[b][b]+=w;L[a][b]-=w;L[b][a]-=w
 return L
def reduced(L,r):return [[v for j,v in enumerate(row) if j!=r] for i,row in enumerate(L) if i!=r]
def run(out):
 out.mkdir(parents=True,exist_ok=True);cases=[];subsets=roots=0
 for n in range(1,6):
  universe=list(itertools.combinations(range(n),2))
  for mask in range(1<<len(universe)):
   E=[e for j,e in enumerate(universe) if mask>>j&1];W=[1+(universe.index(e)%5) for e in E]
   trees=[]
   for S in itertools.combinations(range(len(E)),n-1):
    subsets+=1
    if is_tree(n,[E[j] for j in S]):trees.append(S)
   val=sum(math.prod(W[j] for j in S) for S in trees);L=lap(n,E,W);cof=[]
   for r in range(n):
    C=reduced(L,r);d=det(C);assert d==leibniz(C)==val;roots+=1;cof.append(str(d))
   cases.append({'n':n,'mask':mask,'edges':E,'weights':W,'tree_count':len(trees),'weighted_sum':val,'cofactors':cof})
 rng=random.Random(2026111613);signed=[]
 for case in range(100):
  n=1+case%6;U=list(itertools.combinations(range(n),2));E=[e for e in U if rng.randrange(4)!=0];W=[Fraction(rng.randrange(-3,4),rng.randrange(1,5)) for e in E]
  val=Fraction(0);tc=0
  for S in itertools.combinations(range(len(E)),n-1):
   if is_tree(n,[E[j] for j in S]):val+=math.prod(W[j] for j in S);tc+=1
  ds=[det(reduced(lap(n,E,W),r)) for r in range(n)];assert all(v==val for v in ds)
  signed.append({'n':n,'edges':E,'weights':list(map(str,W)),'tree_count':tc,'tree_sum':str(val),'cofactors':list(map(str,ds))})
 minors=[]
 for n in range(1,7):
  E=list(itertools.combinations(range(n),2));count=nonzero=0
  for S in itertools.combinations(E,n-1):
   tree=is_tree(n,S)
   for r in range(n):
    B=[[int(i==b)-int(i==a) for a,b in S] for i in range(n) if i!=r];v=det(B)
    assert (abs(v)==1) if tree else (v==0);count+=1;nonzero+=int(v!=0)
   # Reversal of every incidence column also preserves squared minors.
   assert det([[-x for x in row] for row in B])**2==v*v
  minors.append({'n':n,'rooted_minors_checked':count,'nonzero':nonzero})
 cb=[]
 for case in range(30):
  k=case%4;m=(case//4)%6;X=[[rng.randrange(-3,4) for _ in range(m)] for _ in range(k)];Y=[[rng.randrange(-3,4) for _ in range(k)] for _ in range(m)]
  XY=[[sum(X[i][s]*Y[s][j] for s in range(m)) for j in range(k)] for i in range(k)]
  lhs=leibniz(XY);rhs=sum(leibniz([[row[j] for j in S] for row in X])*leibniz([Y[j] for j in S]) for S in itertools.combinations(range(m),k));assert lhs==rhs
  cb.append({'X':X,'Y':Y,'k':k,'m':m,'lhs':lhs,'rhs':rhs})
 worked={'n':3,'edges':[[0,1],[0,2],[1,2]],'weights':[2,3,5],'laplacian':lap(3,[(0,1),(0,2),(1,2)],[2,3,5]),'tree_products':[6,10,15],'sum':31}
 for name,value in [('all_graphs.json',cases),('signed_rational_cases.json',signed),('incidence_minors.json',minors),('cauchy_binet_cases.json',cb),('worked_triangle.json',worked)]:
  (out/name).write_text(json.dumps(value,separators=(',',':'))+'\n')
 result={'status':'PASS','classification':'CANDIDATE PROOF','all_labeled_simple_graphs_n1_through5':len(cases),'rooted_cofactors_dual_determinants':roots,'edge_subsets_examined':subsets,'signed_rational_inputs':len(signed),'rooted_incidence_minors':sum(x['rooted_minors_checked'] for x in minors),'cauchy_binet_inputs':len(cb),'seed':2026111613,'formal_checker':False,'external_review':False,'scope':'Finite exact checks; not a proof for arbitrary n or arbitrary real weights. Both routes share author, host, input and Python runtime.'}
 (out/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':run(Path(sys.argv[1] if len(sys.argv)>1 else 'checks'))
