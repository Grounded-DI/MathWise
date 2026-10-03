#!/usr/bin/env python3
"""Supporting exact checks for the four-dimensional minimality follow-up.

Python 3.8+ standard library; run without -O:
  python3 verify_minimality.py --output results_minimality.json
Universal root existence, dimension exclusions, and natural-basis implications
are mathematical arguments in the report, not proved by these check groups.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse
import json
import platform


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def rank_basis(vectors):
    if not vectors:
        return []
    a = [list(map(F, row)) for row in vectors]
    pivot = 0
    for col in range(len(a[0])):
        row = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        lead = a[pivot][col]
        a[pivot] = [x / lead for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return [tuple(row) for row in a[:pivot]]


def identity(n):
    return [tuple(F(i == j) for j in range(n)) for i in range(n)]


def mm(a, b):
    return [[sum(F(x) * F(y) for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, v):
    return tuple(c * x for x in v)


def evo(rows, a, b):
    return tuple(sum(F(a[i]) * F(b[i]) * F(rows[i][j])
                     for i in range(len(rows))) for j in range(len(rows)))


def derived(rows):
    basis = rank_basis(identity(len(rows)))
    dims = [len(basis)]
    for _ in range(len(rows) + 1):
        nxt = rank_basis([evo(rows, a, b) for a in basis for b in basis])
        dims.append(len(nxt))
        if nxt == basis:
            return dims, nxt
        basis = nxt
    raise AssertionError('Derived chain failed to stabilize.')


def mul2(table, x, y):
    aa, ab, bb = table
    return tuple(x[0] * y[0] * aa[j] +
                 (x[0] * y[1] + x[1] * y[0]) * ab[j] +
                 x[1] * y[1] * bb[j] for j in range(2))


def left_matrix(table, x):
    columns = [mul2(table, x, e) for e in identity(2)]
    return [list(row) for row in zip(*columns)]


def det_coefficients(table):
    (p, q), (r, s), (t, u) = table
    return [r * u - t * s, p * u - q * t, p * s - q * r]


# Sparse formal polynomial arithmetic with seven independent variables.
def variable(i):
    e = [0] * 7
    e[i] = 1
    return {tuple(e): 1}


def padd(a, b, factor=1):
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, 0) + factor * coefficient
    return {k: v for k, v in out.items() if v}


def pmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(x + y for x, y in zip(ma, mb))
            out[monomial] = out.get(monomial, 0) + ca * cb
    return {k: v for k, v in out.items() if v}


# Q(i) as rational pairs, avoiding binary floating-point complex arithmetic.
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))


def ga(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gs(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gm(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def gscale(c, a):
    return (F(c) * a[0], F(c) * a[1])


def gmul2(table, x, y):
    aa, ab, bb = table
    cross = ga(gm(x[0], y[1]), gm(x[1], y[0]))
    return tuple(ga(ga(gscale(aa[j], gm(x[0], y[0])),
                       gscale(ab[j], cross)),
                    gscale(bb[j], gm(x[1], y[1]))) for j in range(2))


def audit():
    checks = []

    def passed(identifier, description, evidence):
        checks.append({'id': identifier, 'description': description,
                       'status': 'PASS', 'evidence': evidence})

    W = [(1, 0, -1, 0), (1, 1, 0, 1),
         (0, 1, -1, -1), (0, 0, 1, 1)]
    fs = [(1, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 1)]

    def embed(x):
        return (x[0], x[1], x[2], x[0] + x[2])

    def dproduct(a, b):
        x, y, z = a
        u, v, w = b
        return (x * u + y * v, y * v + z * w, x * w + z * u)

    for a in identity(3):
        for b in identity(3):
            check(evo(W, embed(a), embed(b)) == embed(dproduct(a, b)),
                  'Induced witness product mismatch.')
    passed('M01', 'Witness embedding and all nine basis-product identities',
           {'structure_matrix': W, 'stable_basis': fs, 'identities': 9,
            'product': '(xu+yv, yv+zw, xw+zu)'})

    dims, stable = derived(W)
    check(dims == [4, 3, 3], 'Derived dimensions mismatch.')
    check(stable == rank_basis(fs) == rank_basis(W), 'Stable hyperplane mismatch.')
    check(evo(W, fs[0], fs[0]) == fs[0], 'f1 square mismatch.')
    check(evo(W, fs[1], fs[1]) == add(fs[0], fs[1]), 'f2 square mismatch.')
    check(evo(W, fs[0], fs[2]) == fs[2], 'f1 f3 mismatch.')
    passed('M02', 'Derived chain and spanning products establishing D squared = D',
           {'dimensions': dims, 'hyperplane': 'last coordinate = first + third',
            'stable_row_basis': stable})

    qcols = [evo(W, f, f)[:3] for f in fs]
    qcols += [scale(2, evo(W, fs[i], fs[j])[:3])
              for i, j in combinations(range(3), 2)]
    qrows = [list(row) for row in zip(*qcols)]
    check(qrows == [[1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0]], 'Square-map coefficients mismatch.')
    passed('M03', 'Exact square-map coefficients',
           {'monomials': ['x^2', 'y^2', 'z^2', 'xy', 'xz', 'yz'],
            'coefficients': qrows,
            'scope': 'Exhaustive complex square-zero elimination is the written two-branch proof.'})

    B1 = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
    B2 = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
    B3 = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    B0 = [[B1[i][j] + B2[i][j] for j in range(3)] for i in range(3)]
    inverse = [[1, 0, 0], [0, F(1, 2), 0], [0, 0, 1]]
    check(mm(inverse, B0) == [list(row) for row in identity(3)], 'B0 inverse mismatch.')
    A, C = mm(inverse, B1), mm(inverse, B3)
    AC, CA = mm(A, C), mm(C, A)
    commutator = [[AC[i][j] - CA[i][j] for j in range(3)] for i in range(3)]
    check(commutator == [[0, 0, 1], [0, 0, 0], [-1, 0, 0]], 'Commutator mismatch.')
    passed('M04', 'Invertible reference form and nonzero commutator',
           {'B0': B0, 'B0_determinant': 2, 'commutator': commutator,
            'scope': 'The implication from a natural basis to commuting operators is proved in the report.'})

    p, q, r, s, t, u, lam = [variable(i) for i in range(7)]
    actual = padd(pmul(padd(r, pmul(lam, p)), padd(u, pmul(lam, s))),
                  pmul(padd(t, pmul(lam, r)), padd(s, pmul(lam, q))), -1)
    leading = padd(pmul(p, s), pmul(q, r), -1)
    middle = padd(pmul(p, u), pmul(q, t), -1)
    constant = padd(pmul(r, u), pmul(t, s), -1)
    expected = padd(padd(pmul(leading, pmul(lam, lam)), pmul(middle, lam)), constant)
    check(actual == expected, 'General formal determinant identity mismatch.')
    passed('M05', 'General two-dimensional determinant identity in independent formal variables',
           {'basis_products': ['a^2=(p,q)', 'ab=(r,s)', 'b^2=(t,u)'],
            'determinant': '(ps-qr)lambda^2 + (pu-qt)lambda + (ru-ts)',
            'arithmetic': 'Sparse polynomial coefficients are exact integers.',
            'scope': 'Root existence and the natural-basis proof remain mathematical arguments.'})

    singular = [(1, 0), (1, 0), (0, 1)]
    a, v = (1, 0), (-1, 1)
    check(det2(left_matrix(singular, a)) == 0, 'Singular branch missing.')
    check(mul2(singular, a, v) == (0, 0), 'Singular branch product mismatch.')
    check(det2([[a[0], v[0]], [a[1], v[1]]]) != 0, 'Singular branch dependence.')
    check(mul2(singular, a, a) == a and mul2(singular, v, v) == v,
          'Singular branch basis squares mismatch.')
    passed('M06', 'Initially singular multiplication operator produces a natural basis',
           {'table': singular, 'u': a, 'v': v,
            'basis_squares': ['u^2=u', 'v^2=v'], 'mixed_product': [0, 0]})

    real_complex = [(1, 0), (0, 1), (-1, 0)]
    check(det2(left_matrix(real_complex, (1, 0))) == 1, 'Invertible branch missing.')
    check(det_coefficients(real_complex) == [1, 0, 1], 'Nonreal-root determinant mismatch.')
    gu, gv = (I, ONE), (ONE, I)
    check(gmul2(real_complex, gu, gv) == (ZERO, ZERO), 'Q(i) mixed product mismatch.')
    determinant = gs(gm(gu[0], gv[1]), gm(gu[1], gv[0]))
    check(determinant == (F(-2), F(0)), 'Q(i) basis determinant mismatch.')
    passed('M07', 'Invertible branch with genuinely nonreal determinant roots',
           {'table': real_complex, 'det_L_b_plus_lambda_a': 'lambda^2+1',
            'u': ['i', '1'], 'v': ['1', 'i'], 'basis_determinant': '-2',
            'mixed_product': ['0', '0'],
            'arithmetic': 'Q(i) represented by pairs of rational numbers.',
            'scope': 'Over R this algebra is not an evolution algebra; the field-boundary proof is in the report.'})

    zero_table = [(0, 0), (0, 0), (0, 0)]
    rank_one = [(1, 0), (0, 0), (1, 0)]
    check(mul2(zero_table, (1, 0), (1, 0)) == (0, 0), 'Zero algebra fixture mismatch.')
    check(len(rank_basis(rank_one)) == 1, 'Rank-one multiplication fixture mismatch.')
    check(gmul2(rank_one, (ONE, I), (ONE, I)) == (ZERO, ZERO), 'Rank-one complex nilvector mismatch.')
    passed('M08', 'Degenerate product-image controls',
           {'zero_image_nilvector': [1, 0], 'rank_one_table': rank_one,
            'rank_one_nilvector': ['1', 'i'],
            'scope': 'All product images of dimension <=1 are excluded by the written homogeneous-quadratic argument.'})

    dual = [(1, 0), (0, 1), (0, 0)]
    check(det_coefficients(dual) == [0, 0, 1], 'Dual-number determinant mismatch.')
    check(mul2(dual, (0, 1), (0, 1)) == (0, 0), 'Dual-number nilvector mismatch.')
    check(left_matrix(dual, (0, 1)) == [[0, 0], [1, 0]], 'Dual-number kernel mismatch.')
    passed('M09', 'Square-zero hypothesis control: dual-number multiplication',
           {'table': dual, 'nonzero_square_zero_vector': [0, 1],
            'det_L_xa_plus_yb': 'x^2',
            'scope': 'Failure to admit a natural basis without the square-zero-free hypothesis is proved in the report.'})

    return {'status': 'PASS', 'check_groups': len(checks), 'checks': checks,
            'python_version': platform.python_version(),
            'dependencies': 'Python 3.8+ standard library',
            'arithmetic': 'fractions.Fraction, integer sparse polynomials, rational-pair Q(i)',
            'universal_conclusions': 'Supplied by the report; successful execution is supporting evidence.',
            'exclusions': ['No exhaustive classification search', 'No proof-assistant verification',
                'No machine proof of complex root existence or all dimension exclusions',
                'No historical novelty or AI-provenance determination']}


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = audit()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True,
            default=encode) + '\n', encoding='utf-8')
    print('PASS: %s supporting exact check groups; universal proof supplied separately.' % result['check_groups'])
    for entry in result['checks']:
        print(entry['id'] + ' PASS: ' + entry['description'])
