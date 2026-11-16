#!/usr/bin/env python3
"""Standalone finite-witness checks for MathWise 2026-11-16 public register.
New publication checker, not an original sealed research artifact.
Python standard library only.
"""
from itertools import combinations
from collections import Counter

def quadratic_zero_sum():
    a = (0, 0, 0, 1, 2, 2, 3)
    hits = [ix for ix in combinations(range(7), 4) if sum(a[i] for i in ix) % 4 == 0]
    assert len(hits) == 7
    assert max(Counter(a).values()) == 3
    assert len(hits) < 9
    print("PASS quadratic-zero-sum: 7 < 9; 35 combinations examined")

def independence():
    edges = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
             (1,2),(1,3),(1,5),(2,3),(2,4),(2,6),(2,7),
             (3,4),(3,5),(3,6),(3,8),(4,5),(4,6),(4,9),
             (5,8),(5,9),(6,7),(6,8),(6,9),(7,9),(8,9)]
    assert len(edges) == 28 and len(set(edges)) == 28
    counts = [0] * 11
    for mask in range(1 << 10):
        if all(not (mask & (1 << u) and mask & (1 << v)) for u,v in edges):
            counts[mask.bit_count()] += 1
    while counts[-1] == 0:
        counts.pop()
    assert counts == [1,10,17,4,1], counts
    assert counts[3]**2 < counts[2]*counts[4]
    print("PASS independence polynomial: (1,10,17,4,1); 1024 subsets examined")

def spanning_tree():
    # Two K5 cliques, plus cross edges (0,5) and (1,6).
    from itertools import combinations
    edges = list(combinations(range(5),2)) + list(combinations(range(5,10),2)) + [(0,5),(1,6)]
    assert len(edges) == 22
    total = containing = 0
    for chosen in combinations(range(len(edges)), 9):
        parent = list(range(10))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        valid = True
        for j in chosen:
            u,v = edges[j]
            ru,rv = root(u),root(v)
            if ru == rv:
                valid = False
                break
            parent[ru] = rv
        if valid and len({root(i) for i in range(10)}) == 1:
            total += 1
            containing += 0 in chosen if edges[0] == (0,5) else 20 in chosen
    assert (total, containing) == (43750,28125), (total,containing)
    assert 2*containing > total
    print("PASS spanning tree: 28125 / 43750 = 9/14 > 1/2; 497420 subsets examined")

if __name__ == "__main__":
    quadratic_zero_sum()
    independence()
    spanning_tree()
