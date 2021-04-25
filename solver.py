from z3 import *

# assuming all variables are integers
def convert_program_to_constraints(filename: str) -> list:
    f = open(filename, "r")
    lines = f.readlines()
    list_of_constraints = []
    list_of_variables = []

    idx = 0
    while (idx < len(lines)):
        line = lines[idx].strip()

        # start of a clause
        if "{" in line:
            pass

        idx += 1


'''
    for line in lines:
        line = line.strip()
        
        # assignment 
        if "=" in line:
            pass
        # implies
        elif "while" in line:

'''


def main():

    convert_program_to_constraints("test.txt")

    s = Solver()
    x = Int('x')
    y = Int('y')
    solve(x > 2, y < 10, x + 2*y == 7)
    print(simplify(x + y + 2*x + 3))
    print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))


if __name__ == "__main__":
    main()