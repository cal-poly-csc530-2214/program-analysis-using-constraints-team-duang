from z3 import *


def main():
    s = Solver()
    x = Int('x')
    y = Int('y')
    solve(x > 2, y < 10, x + 2*y == 7)
    print(simplify(x + y + 2*x + 3))
    print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))


if __name__ == "__main__":
    main()