#!/usr/bin/env python3
"""Exact checks for the Barei evolution-algebra audit. Python standard library only.

Run: python3 verify_audit.py --output results.json
This verifies the finite computations, not the universal geometric theorem.
The report supplies the exhaustive branch proofs and algebraic dependencies.
"""
from fractions import Fraction as F
from itertools import product as tuples
from pathlib import Path
import argparse
import json
import platform


def eye(n):
    return [tuple(F(i == j) for j in range(n)) for i in range(n)]


def transpose(a):
    return [tuple(row) for row in zip(*a)]


def matvec(a, x):
    return tuple(sum(F(v) * w for v, w in zip(row, x)) for row in a)


def matmul(a, b):
    return [tuple(sum(F(a[i][k]) * b[k][j] for k in range(len(b)))
                  for j in range(len(b[0]))) for i in range(len(a))]


def submat(a, b):
    return [tuple(F(x) - y for x, y in zip(ra, rb)) for ra, rb in zip(a, b)]


def add(a, b):
    return tuple(F(x) + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(F(c) * x for x in a)


def rref(vectors, p=None):
    if not vectors:
        return []
    a = [[int(x) % p if p else F(x) for x in v] for v in vectors]
    pivot = 0
    for j in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][j]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        inv = pow(a[pivot][j], -1, p) if p else 1 / a[pivot][j]
        a[pivot] = [(x * inv) % p if p else x * inv for x in a[pivot]]
        for i in range(len(a)):
            if i == pivot:
                continue
            factor = a[i][j]
            a[i] = [(a[i][k] - factor * a[pivot][k]) % p if p else
                    a[i][k] - factor * a[pivot][k] for k in range(len(a[0]))]
        pivot += 1
        if pivot == len(a):
            break
    return [tuple(row) for row in a[:pivot]]


def evo_mul(rows, a, b, p=None):
    value = tuple(sum(F(a[i]) * b[i] * rows[i][j] for i in range(len(rows)))
                  for j in range(len(rows)))
    return tuple(int(x) % p for x in value) if p else value


def derived(rows, p=None):
    basis = rref(eye(len(rows)), p)
    trace = [len(basis)]
    for _ in range(len(rows) + 1):
        new = rref([evo_mul(rows, a, b, p) for a in basis for b in basis], p)
        trace.append(len(new))
        if new == basis:
            return trace, new
        basis = new
    raise AssertionError("finite derived chain did not stabilize")


def finite_solutions(rows, p, idempotent):
    return [list(v) for v in tuples(range(p), repeat=len(rows))
            if evo_mul(rows, v, v, p) == (v if idempotent else (0,) * len(rows))]


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def audit():
    checks = []

    def passed(identifier, description, evidence):
        checks.append(dict(id=identifier, status="PASS", description=description,
                           evidence=evidence))

    # Input conventions: row i of M is e_i squared; distinct natural vectors multiply to zero.
    M = [(-2, 0, 2), (0, 1, -1), (0, -1, 1)]
    r1, r2, r3 = M
    assert r3 == scale(-1, r2)
    values = [evo_mul(M, r1, r1), evo_mul(M, r1, r2), evo_mul(M, r2, r2)]
    assert values == [scale(4, add(r1, scale(-1, r2))), scale(2, r2), (0, 0, 0)]
    passed("C01", "Published multiplication identities reconstructed from the matrix",
           dict(r1_squared=values[0], r1_r2=values[1], r2_squared=values[2]))

    dims, stable = derived(M)
    assert dims == [3, 2, 2]
    assert rref(stable) == rref([r1, r2])
    passed("C02", "Derived chain has a nonzero stable term",
           dict(dimensions=dims, stable_basis=stable))

    # Exhaustive proof over C (indeed any field of characteristic not two):
    # x=-2x^2 -> x=0 or -1/2. Put s=y+z=2x^2.
    # y=y^2-z^2=(y-z)s=(2y-s)s -> (1-2s)y=-s^2.
    branches = []
    for x in [F(0), F(-1, 2)]:
        s = 2*x*x
        lhs_coefficient, rhs = 1-2*s, -s*s
        if lhs_coefficient:
            y = rhs / lhs_coefficient
            z = s-y
            v = (x, y, z)
            assert evo_mul(M, v, v) == v == (0, 0, 0)
            branches.append(dict(x=x, outcome="zero solution", solution=v))
        else:
            assert rhs != 0
            branches.append(dict(x=x, outcome="inconsistent", equation="0 = -1/4"))
    passed("C03", "All idempotent branches exhausted analytically",
           dict(solution=[0, 0, 0], branches=branches,
                scope="complex solutions; no numeric approximation or bounded search"))

    H = [(-1, 0, -1), (-2, 2, 0), (1, 0, 1)]
    # Columns are phi(e1)=-h2, phi(e2)=h3, phi(e3)=-h1.
    P = [(0, 0, -1), (-1, 0, 0), (0, 1, 0)]
    assert len(rref(transpose(P))) == 3
    for a in eye(3):
        for b in eye(3):
            assert matvec(P, evo_mul(M, a, b)) == evo_mul(H, matvec(P, a), matvec(P, b))
    passed("C04", "Barei example is isomorphic to Hu-Wen E_2",
           dict(change_of_basis=P, images=["e1 -> -h2", "e2 -> h3", "e3 -> -h1"],
                basis_product_equalities=9))

    # An independently constructed strictness witness for Corollary 3.4 vs Hu-Wen Prop. 2.8.
    W = [(1, 0, -1, 0), (1, 1, 0, 1), (0, 1, -1, -1), (0, 0, 1, 1)]
    T = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1)]
    wdims, wbasis = derived(W)
    assert wdims == [4, 3, 3]
    assert rref(transpose(T)) == wbasis

    def dmul(a, b):
        x, y, z = a
        u, v, w = b
        return (x*u+y*v, y*v+z*w, x*w+z*u)

    for a in eye(3):
        for b in eye(3):
            assert evo_mul(W, matvec(T, a), matvec(T, b)) == matvec(T, dmul(a, b))
    passed("C05", "Strictness witness: E squared is the indicated three-dimensional algebra",
           dict(structure_matrix=W, dimensions=wdims, embedding=T,
                square_map="(x^2+y^2, y^2+z^2, 2xz)", basis_product_equalities=9))

    B1 = [(1, 0, 0), (0, 1, 0), (0, 0, 0)]
    B2 = [(0, 0, 0), (0, 1, 0), (0, 0, 1)]
    B3 = [(0, 0, 1), (0, 0, 0), (1, 0, 0)]
    B0_inv = [(1, 0, 0), (0, F(1, 2), 0), (0, 0, 1)]
    A, C = matmul(B0_inv, B1), matmul(B0_inv, B3)
    commutator = submat(matmul(A, C), matmul(C, A))
    assert commutator == [(0, 0, 1), (0, 0, 0), (-1, 0, 0)]
    # Simultaneous congruence diagonalization would make B0^-1 B1 and B0^-1 B3
    # simultaneously diagonal under similarity, hence commuting. They do not.
    idem = matvec(T, (1, 0, 0))
    assert evo_mul(W, idem, idem) == idem
    passed("C06", "Strictness witness: stable term is not an evolution algebra",
           dict(nonzero_commutator=commutator, nonzero_idempotent=idem,
                square_zero_proof="2xz=0 -> x=0 or z=0 -> remaining squares zero -> x=y=z=0",
                scope="N(D)=0 over C proved in report; commutator obstruction exact"))

    # Deliberately outside the algebraically closed field hypothesis.
    F3 = [(1, 2), (1, 1)]
    nils, idems = finite_solutions(F3, 3, False), finite_solutions(F3, 3, True)
    assert nils == idems == [[0, 0]]
    assert derived(F3, 3)[0] == [2, 2]
    passed("C07", "Scope test: F_3 has a perfect, square-zero-free, idempotent-free example",
           dict(field="F_3", structure_matrix=F3, points_enumerated=9,
                square_zero_elements=nils, idempotents=idems,
                classification="outside theorem hypothesis; no contradiction over algebraic closure"))

    # The original numeric example degenerates in characteristic two.
    c2dims, _ = derived(M, 2)
    assert c2dims == [3, 1, 0, 0]
    passed("C08", "Scope test: Barei's particular example is solvable in characteristic two",
           dict(field="F_2", dimensions=c2dims))

    # The new sufficient condition is not necessary for the equivalence in an individual E.
    U = [(1, -1, 0), (0, -1, -1), (0, 1, 1)]
    u, v = (1, 0, 1), (0, 1, 1)
    assert derived(U)[0] == [3, 2, 2]
    assert evo_mul(U, u, u) == u
    assert evo_mul(U, u, v) == v
    assert evo_mul(U, v, v) == (0, 0, 0)
    passed("C09", "Scope test: N(D)=0 is sufficient, not necessary for the equivalence",
           dict(structure_matrix=U, stable_basis=[u, v], nonzero_idempotent=u,
                nonzero_square_zero_element=v, stable_algebra="dual numbers"))

    # Deliberate coefficient mutation: delete the +2 e3 term of e1 squared.
    mutated = [(-2, 0, 0), (0, 1, -1), (0, -1, 1)]
    candidate = (F(-1, 2), 0, 0)
    assert evo_mul(mutated, candidate, candidate) == candidate
    assert evo_mul(M, candidate, candidate) != candidate
    passed("C10", "Negative control detects a coefficient change that destroys idempotent-freeness",
           dict(mutation="row 1 column 3: 2 -> 0", new_nonzero_idempotent=candidate))

    # A square-zero-free vector subspace without multiplication closure is insufficient.
    e1 = (1, 0, 0)
    assert evo_mul(M, e1, e1) == (-2, 0, 2)
    assert len(rref([e1, evo_mul(M, e1, e1)])) == 2
    passed("C11", "Scope test: arbitrary square-zero-free lines need not contain idempotents",
           dict(line="C e1 in Barei E_0", square=evo_mul(M, e1, e1),
                missing_hypothesis="multiplication closure / V squared = V"))

    return dict(status="PASS", scope="Exact finite computations and stated exhaustive branch checks",
                exclusions=["not a proof-assistant formalization", "not a machine proof of universal fixed-point or Bezout theorem",
                            "not independent verification of author interaction histories", "not a novelty search over all literature"],
                python_version=platform.python_version(), arithmetic="fractions.Fraction and finite-field integers",
                required_dependencies="Python standard library only", check_groups=len(checks), checks=checks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit()
    text = json.dumps(result, default=encode, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print("PASS: %d exact check groups; scope limitations retained." % result["check_groups"])
    for item in result["checks"]:
        print(item["id"] + " PASS: " + item["description"])
