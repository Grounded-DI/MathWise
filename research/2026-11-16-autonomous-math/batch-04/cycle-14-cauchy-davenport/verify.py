from pathlib import Path
from itertools import product
from math import prod
import json,sys,random
p=Path(sys.argv[1]);p.mkdir(exist_ok=True)
rows=[];poly=[];counts={};rng=random.Random(2026111614)
def check(q,a,b):
 A=[i for i in range(q) if a>>i&1];B=[i for i in range(q) if b>>i&1]
 sums=sorted({(x+y)%q for x in A for y in B});mask=0;full=(1<<q)-1
 for x in A:mask|=((b<<x)|(b>>(q-x)))&full
 assert mask==sum(1<<s for s in sums)
 bound=min(q,len(A)+len(B)-1);assert len(sums)>=bound
 rows.append([q,a,b,sums,bound])
for q in [2,3,5,7]:
 before=len(rows)
 for a in range(1,1<<q):
  for b in range(1,1<<q):check(q,a,b)
 counts[q]=len(rows)-before
for q in [11,13,17,19,23,29,31]:
 for _ in range(30):check(q,rng.randrange(1,1<<q),rng.randrange(1,1<<q))
# Verify coefficient identity on every monomial basis element of each bounded polynomial space.
for q in [2,3,5]:
 for a in range(1,1<<q):
  for b in range(1,1<<q):
   A=[i for i in range(q) if a>>i&1];B=[i for i in range(q) if b>>i&1];m=len(A);n=len(B)
   wa=[pow(prod((x-y)%q for y in A if y!=x)%q,-1,q) for x in A]
   wb=[pow(prod((x-y)%q for y in B if y!=x)%q,-1,q) for x in B]
   for i in range(m+n-1):
    for j in range(m+n-1-i):
     val=sum(pow(x,i,q)*u for x,u in zip(A,wa))*sum(pow(x,j,q)*u for x,u in zip(B,wb))%q
     expected=int(i==m-1 and j==n-1);assert val==expected
     poly.append([q,a,b,i,j,val])
# Every size pair has an interval equality example.
sharp=[]
for q in [2,3,5,7,11,13]:
 for m in range(1,q+1):
  for n in range(1,q+1):
   S={(a+b)%q for a in range(m) for b in range(n)};assert len(S)==min(q,m+n-1);sharp.append([q,m,n,len(S)])
negative={'modulus':4,'A':[0,2],'B':[0,2],'sumset':[0,2],'size':2,'naive_bound':3};assert len({(a+b)%4 for a in [0,2] for b in [0,2]})==2
result={'exhaustive_pairs_by_prime':counts,'exhaustive_total':sum(counts.values()),'seed':2026111614,'larger_sample_pairs':210,'sample_primes':[11,13,17,19,23,29,31],'coefficient_monomial_checks':len(poly),'sharpness_cases':len(sharp),'all_pass':True,'composite_negative_control':negative}
for name,obj in [('results.json',result),('sumsets.json',rows),('coefficient_checks.json',poly),('sharpness.json',sharp)]: (p/name).write_text(json.dumps(obj,separators=(',',':'))+'\n')
print(json.dumps(result,indent=2))
