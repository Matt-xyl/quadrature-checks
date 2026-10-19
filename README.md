# Quadrature Checks

A small Python command-line program for inspecting numerical integration. It compares the composite trapezoidal and Simpson rules at two resolutions and shows their absolute error against a known integral.

The examples use functions with exact integrals, since this lets us check the computed estimates directly. The difference between two resolutions is also shown, but that difference alone is not a proved bound on the true error.

## Run it

Python 3.10 or later is enough. No third-party packages or API keys are needed.

```sh
python quadrature.py --function sine --n 8
python quadrature.py --function cubic --n 4
python -m unittest -v
```

`--function` accepts `sine`, `square`, `cubic`, or `exponential`. `--n` is a positive even number of equal subintervals; the program also evaluates `2n`. With `n` subintervals, each rule samples `n+1` nodes.

| Example | Interval | Known integral |
| --- | --- | --- |
| sine | 0 to pi | 2 |
| square | 0 to 1 | 1/3 |
| cubic | 0 to 1 | 1/4 |
| exponential | 0 to 1 | e - 1 |

## What to look at

For the cubic example, Simpson's rule reproduces the known integral up to floating-point arithmetic. For sine, refining the grid usually reduces the computed error. Run both rules and compare their estimates, refinement differences, and error against the known value.

The formulas are implemented in short functions in [quadrature.py](quadrature.py). The [tests](test_quadrature.py) check an exact polynomial case, refinement on sine, a reversed interval, and invalid inputs. These are demonstration checks, not a proof of an error bound for an arbitrary function.

## Scope and authorship

This is a learning project maintained by [Matt-xyl](https://github.com/Matt-xyl). The implementation, tests, and documentation were prepared with AI assistance. It demonstrates a working artifact; it is not presented as independently written code or as a result from a private research study.

The program uses fixed demonstration functions. It does not evaluate arbitrary input code or read private files. It is intended for small experiments with smooth functions on finite intervals. It does not handle singular integrals or adaptive error control, and the displayed known integrals use Python floating-point values.

Released under the [MIT license](LICENSE).
