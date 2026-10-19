"""Compare simple quadrature estimates with known demonstration integrals."""
import argparse
import math


def _check_n(n, *, even=False):
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')
    if even and n % 2:
        raise ValueError("Simpson's rule requires an even n")


def trapezoidal(f, a, b, n):
    """Composite trapezoidal rule with n equal subintervals."""
    _check_n(n)
    h = (b - a) / n
    interior = math.fsum(f(a + i * h) for i in range(1, n))
    return h * (0.5 * f(a) + interior + 0.5 * f(b))


def simpson(f, a, b, n):
    """Composite Simpson rule with an even number of subintervals."""
    _check_n(n, even=True)
    h = (b - a) / n
    odd = math.fsum(f(a + i * h) for i in range(1, n, 2))
    even = math.fsum(f(a + i * h) for i in range(2, n, 2))
    return h / 3 * (f(a) + 4 * odd + 2 * even + f(b))


EXAMPLES = {
    'sine': (math.sin, 0.0, math.pi, 2.0),
    'square': (lambda x: x * x, 0.0, 1.0, 1 / 3),
    'cubic': (lambda x: x ** 3, 0.0, 1.0, 1 / 4),
    'exponential': (math.exp, 0.0, 1.0, math.e - 1),
}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--function', choices=EXAMPLES, default='sine')
    parser.add_argument('--n', type=int, default=8,
                        help='positive even subinterval count (default: 8)')
    args = parser.parse_args(argv)
    try:
        _check_n(args.n, even=True)
    except ValueError as error:
        parser.error(str(error))
    f, a, b, known = EXAMPLES[args.function]
    print(f'{args.function}: interval [{a:.10g}, {b:.10g}]')
    print(f'Known integral (floating-point reference): {known:.12g}')
    print(f'{"Rule":<14} {"n":>6} {"Estimate":>18} {"Absolute error":>18}')
    for name, rule in [('Trapezoidal', trapezoidal), ('Simpson', simpson)]:
        estimates = []
        for n in (args.n, 2 * args.n):
            estimate = rule(f, a, b, n)
            estimates.append(estimate)
            print(f'{name:<14} {n:>6} {estimate:>18.12g} {abs(estimate-known):>18.8g}')
        print(f'  Difference between estimates: {abs(estimates[1]-estimates[0]):.8g}')
    print('A refinement difference alone is not a proved true-error bound.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
