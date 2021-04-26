from z3 import *

def getAlterCondition(condition):
    items = condition.split(" ")

    if items[1] == '<':
        items[1] = '>='
    elif items[1] == '>':
        items[1] = '<='
    elif items[1] == '>=':
        items[1] = '<'
    elif items[1] == '<=':
        items[1] = '>'

    return " ".join(items)

# assuming all variables are integers
def convert_program_to_constraints(filename: str) -> list:
    f = open(filename, "r")
    lines = f.readlines()
    list_of_constraints = []

    idx = 0
    start = False

    constraint = "true => "
    alterCondition = ""
    while (idx < len(lines)):
        line = lines[idx].strip()

        # start of a clause
        if "while" in line:
            start = True
            condition = line[line.find("(") + 1: line.find(")")]
            alterCondition = getAlterCondition(condition)
            constraint += "I \u2227 " + condition + " => I["
            # one constraint util "{...}"
            # while constraint => I[while loop]
            #(x+y)/x   (after) / before
        if "=" in line:
            before = line[:line.find("=")]
            after = line[line.find("=") + 1:]
            
            if (start == False):
                constraint += "I[({0} ) / {1}]".format(after, before)
                list_of_constraints.append(constraint)
                constraint = ""
            else:
                constraint += "({0} ) / {1}".format(after, before)
                constraint += ", "
        if "++" in line:
            before = line[:line.find("+")]
            constraint += "({0} + 1) / {0}".format(before)
            if (start == False):
                list_of_constraints.append(constraint)
                constraint = ""
            else:
                constraint += ", "
        if "--" in line:
            before = line[:line.find("+")]
            constraint += "({0} - 1) / {0}".format(before)
            if (start == False):
                list_of_constraints.append(constraint)
                constraint = ""
            else:
                constraint += ", "
        if "}" in line and start == True:
            start = False
            constraint = constraint[:-2]
            constraint += "]"
            list_of_constraints.append(constraint)
            constraint = "I \u2227 " + alterCondition
        if "assert" in line:
            assertion = line[line.find("(") + 1: line.find(")")]
            constraint = constraint + " => " + assertion
            list_of_constraints.append(constraint)

        idx += 1

    return list_of_constraints

def solve_with_z3(list_of_constraints: list):
    x, y = Bools('x y')

    
    s = Solver()

    print(s.check())


'''
declare x0, a0 // initial values
declare a1, x1 // values after first unrolling
x0 > 10 && x0 < 100 ==> a1 == a0 + x0 && x1 == x0 + 1
declare a2, x2 // values after second unrolling
x1 > 10 && x1 < 100 ==> a2 == a1 + x1 && x2 == x1 + 1

'''

'''
# declare variables
x = Int('x')
y = Int('y')

s = Solver()

true implies I[-50 / x]
I and x < 0 implies I[y+1]/y , (x+y)/x)
I and x >= 0 implies y > 0

s.add(x = -50, while loop, y > 0) //start cut point

s.check()

'''

def main():

    list_of_constraints = convert_program_to_constraints("test.txt")

    for item in list_of_constraints:
        print(item)

    solve_with_z3(list_of_constraints)


if __name__ == "__main__":
    main()
