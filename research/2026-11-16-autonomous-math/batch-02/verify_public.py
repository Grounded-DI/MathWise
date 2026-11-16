#!/usr/bin/env python3
"""Batch 02 public smoke checks (new standalone code, not original sealed verifiers).
Run: python3 verify_public.py. Uses standard library, finite cases only.
"""
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial

def prufer_edges(word, n):
    deg=[0]+[1+word.count(v) for v in range(1,n+1)]
    edges=[]
    for v in word:
        leaf=next(i for i in range(1,n+1) if deg[i]==1)
        edges.append(tuple(sorted((leaf,v))))
        deg[leaf]-=1;deg[v]-=1
    u,v=[i for i in range(1,n+1) if deg[i]==1]
    edges.append((u,v))
    return tuple(sorted(edges))

def cayley():
    for n in range(2,7):
        trees={prufer_edges(w,n) for w in product(range(1,n+1),repeat=n-2)}
        assert len(trees)==n**(n-2)
    print("PASS Cayley finite decoding n=2..6")

def egz():
    cases=0
    for n in range(2,5):
        for a in combinations_with_replacement(range(n),2*n-1):
            assert any(sum(a[i] for i in ix)%n==0 for ix in combinations(range(2*n-1),n))
            cases+=1
    print("PASS EGZ finite residue multisets",cases)

def lucas():
    for p in (2,3,5,7):
        for n in range(0,100):
            for k in range(n+1):
                a,b=n,k;out=1
                while a or b:
                    na,nb=a%p,b%p
                    out=(out*(comb(na,nb) if nb<=na else 0))%p
                    a//=p;b//=p
                assert comb(n,k)%p==out
    print("PASS Lucas finite n<100, primes 2,3,5,7")

def dilworth_b3():
    sets=list(range(8))
    chains=[];anti=[]
    for mask in range(1,256):
        group=[s for s in sets if mask>>s&1]
        if all((a&b)==a or (a&b)==b for a,b in combinations(group,2)):chains.append(mask)
        if all((a&b)!=a and (a&b)!=b for a,b in combinations(group,2)):anti.append(mask)
    width=max(m.bit_count() for m in anti)
    dp=[99]*256;dp[0]=0
    for m in range(1,256):
        dp[m]=1+min(dp[m^c] for c in chains if c&m==c)
    assert width==dp[255]==3
    print("PASS Dilworth Boolean lattice B3")

def sperner():
    for n in range(0,4):
        subset_count=1<<n
        rank=[comb(n,r) for r in range(n+1)]
        for fam in range(1<<subset_count):
            h=[0]*subset_count
            for s in range(subset_count):
                h[s]=(1 if fam>>s&1 else 0)+max((h[s^(1<<i)] for i in range(n) if s>>i&1),default=0)
            k=max(h,default=0)
            assert fam.bit_count()<=sum(sorted(rank,reverse=True)[:k])
    print("PASS generalized Sperner n=0..3 all families")

def small_controls():
    # Uniform triangle has 3 trees, each edge in 2, each pair in 1.
    assert 1*3-2*2 < 0
    # Doubly stochastic convex mixture of two permutation matrices.
    p1=((1,0,0),(0,1,0),(0,0,1))
    p2=((0,1,0),(0,0,1),(1,0,0))
    A=[[ (p1[i][j]+p2[i][j])/2 for j in range(3)] for i in range(3)]
    assert all(sum(row)==1 for row in A)
    assert all(sum(A[i][j] for i in range(3))==1 for j in range(3))
    print("PASS weighted-tree / Birkhoff illustrative controls")

if __name__=="__main__":
    cayley();egz();lucas();dilworth_b3();sperner();small_controls()
    print("PUBLIC SMOKE CHECKS PASS — not formal or exhaustive proof certification")
