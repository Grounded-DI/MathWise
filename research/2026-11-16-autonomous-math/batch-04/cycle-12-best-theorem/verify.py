"""Exact bounded BEST verification. Python standard library only. No randomness."""
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction
from math import factorial, prod
import json, sys, hashlib

def det(a):
    a=[[Fraction(x) for x in row] for row in a]; ans=Fraction(1)
    for k in range(len(a)):
        j=next((j for j in range(k,len(a)) if a[j][k]),None)
        if j is None:return 0
        if j!=k:a[j],a[k]=a[k],a[j];ans=-ans
        pivot=a[k][k];ans*=pivot
        for j in range(k+1,len(a)):
            q=a[j][k]/pivot
            for i in range(k+1,len(a)):a[j][i]-=q*a[k][i]
    assert ans.denominator==1
    return int(ans)

def strong(n,arcs):
    for s in range(n):
        seen={s}
        while True:
            nxt=seen|{b for a,b in arcs if a in seen}
            if nxt==seen:break
            seen=nxt
        if len(seen)!=n:return False
    return True

def is_tree(n,arcs,choice,r):
    parents={arcs[e][0]:arcs[e][1] for e in choice}
    if len(parents)!=n-1 or r in parents:return False
    for s in range(n):
        seen=set();v=s
        while v!=r:
            if v in seen or v not in parents:return False
            seen.add(v);v=parents[v]
    return True

def direct_tours(n,arcs,e):
    r=arcs[e][0];out=[[i for i,(a,b) in enumerate(arcs) if a==v] for v in range(n)]
    tours=set();m=len(arcs)
    def walk(v,path,used):
        if len(path)==m:
            if v==r:tours.add(tuple(path))
            return
        for i in out[v]:
            if not (used>>i)&1:walk(arcs[i][1],path+[i],used|(1<<i))
    walk(arcs[e][1],[e],1<<e)
    return tours

def from_orders(n,arcs,orders,e):
    v=arcs[e][0];pos=[0]*n;path=[]
    while pos[v]<len(orders[v]):
        edge=orders[v][pos[v]];pos[v]+=1;path.append(edge);v=arcs[edge][1]
    assert len(path)==len(arcs) and v==arcs[e][0] and path[0]==e
    assert len(set(path))==len(arcs)
    return tuple(path)

def check_graph(n,arcs,name):
    arcs=[tuple(x) for x in arcs];out=[[i for i,(a,b) in enumerate(arcs) if a==v] for v in range(n)]
    assert all(a!=b for a,b in arcs) and strong(n,arcs)
    assert all(len(out[v])==sum(b==v for a,b in arcs)>0 for v in range(n))
    L=[[0]*n for _ in range(n)]
    for a,b in arcs:L[a][a]+=1;L[a][b]-=1
    roots=[];fixed=[];cert=[]
    for r in range(n):
        verts=[v for v in range(n) if v!=r]
        candidates=list(product(*(out[v] for v in verts)))
        trees=[t for t in candidates if is_tree(n,arcs,t,r)]
        determinant=det([[L[a][b] for b in verts] for a in verts])
        assert len(trees)==determinant>0
        roots.append({'root':r,'assignments_tested':len(candidates),'tree_count':len(trees),'determinant':determinant})
        for e in out[r]:
            direct=direct_tours(n,arcs,e);constructed=set();encoded=set()
            for tree in trees:
                tree_by_tail={arcs[i][0]:i for i in tree}
                options=[]
                for v in range(n):
                    if v==r:options.append([(e,)+q for q in permutations([i for i in out[v] if i!=e])])
                    else:
                        last=tree_by_tail[v]
                        options.append([q+(last,) for q in permutations([i for i in out[v] if i!=last])])
                for orders in product(*options):
                    tour=from_orders(n,arcs,orders,e)
                    assert tour not in constructed
                    constructed.add(tour)
            for tour in direct:
                orders=tuple(tuple(i for i in tour if arcs[i][0]==v) for v in range(n))
                tree=tuple(orders[v][-1] for v in verts)
                assert is_tree(n,arcs,tree,r)
                assert from_orders(n,arcs,orders,e)==tour
                encoded.add(orders)
            expected=len(trees)*prod(factorial(len(x)-1) for x in out)
            assert len(direct)==len(constructed)==len(encoded)==expected and direct==constructed
            fixed.append({'first_arc':e,'root':r,'tour_count':len(direct),'formula':expected})
            cert.append({'first_arc':e,'tours':[list(t) for t in sorted(direct)]})
    return {'name':name,'n':n,'arcs':arcs,'degrees':[len(x) for x in out],'roots':roots,'fixed_arcs':fixed},cert

def main(destination):
    p=Path(destination);p.mkdir(parents=True,exist_ok=True)
    records=[];certificates=[];masks=0;by_n={}
    for n in range(2,5):
        potential=[(a,b) for a in range(n) for b in range(n) if a!=b];count=0
        for mask in range(1<<len(potential)):
            masks+=1;arcs=[e for i,e in enumerate(potential) if (mask>>i)&1]
            if not all(sum(a==v for a,b in arcs)==sum(b==v for a,b in arcs)>0 for v in range(n)):continue
            if not strong(n,arcs):continue
            row,cert=check_graph(n,arcs,f'simple_n{n}_mask{mask}')
            records.append(row);certificates.append({'name':row['name'],'certificates':cert});count+=1
        by_n[str(n)]=count
    simple_count=len(records)
    controls=[]
    for k in range(2,5):controls.append((2,[(0,1)]*k+[(1,0)]*k,f'two_vertices_{k}_parallel'))
    for n in (3,4):
        for k in (2,3):controls.append((n,[(v,(v+1)%n) for v in range(n) for _ in range(k)],f'cycle_n{n}_multiplicity{k}'))
    controls.append((3,[(0,1),(1,2),(2,0),(0,1),(1,0)],'unequal_degrees_parallel'))
    for n,arcs,name in controls:
        row,cert=check_graph(n,arcs,name);records.append(row);certificates.append({'name':name,'certificates':cert})
    result={'simple_masks_examined':masks,'simple_graphs_by_n':by_n,'simple_graphs_accepted':simple_count,'multigraph_controls':len(controls),'total_graphs':len(records),'root_cofactors':sum(len(r['roots']) for r in records),'parent_assignments_tested':sum(x['assignments_tested'] for r in records for x in r['roots']),'fixed_arc_cases':sum(len(r['fixed_arcs']) for r in records),'direct_tours_and_inverse_tests':sum(x['tour_count'] for r in records for x in r['fixed_arcs']),'constructed_order_tuples':sum(x['tour_count'] for r in records for x in r['fixed_arcs']),'all_equal':True,'arithmetic':'exact integers and Fraction; no random inputs'}
    for name,obj in [('results.json',result),('inputs_and_counts.json',records),('tour_certificates.json',certificates)]:
        (p/name).write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'checks')
