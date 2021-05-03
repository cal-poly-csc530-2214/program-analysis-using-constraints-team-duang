# program-analysis-using-constraints-team-duang
program-analysis-using-constraints-team-duang created by GitHub Classroom

From a program generates and sloves a satisifability problem related to the problem input. The problem is translated into a series of constraints that are solved using off-theshelf constraint solvers to yield desired program invariants.
This work is using the paper Program Analysis as Constraint Solving by Gulwani et al

Our goal is to re-create a constraint-based invariant generatior described in the program verification section of the paper. We first created test programs shown in the paper in a text file. Then we read in the program as a string and converted the program into a list of constraints as we go through the lines. Lastly, we tried to convert the list of constraints into readable sat algebra that could feed into python's z3 solver.

The current output of our convert_program_to_constraints is the invariants and constraints of pv1 from the paper. As explained above this will work on all like written programs and can thus be used as a template for the code.
These can then be converted and run via a sat solver such as Z3 but would need to be formated in the correct outpuit for the 
solver. This is on out TODO list but further practice and understanding of the Z3 language is required.

The work we did in the second week (the optional extended assignment) is working with the Z3 to generate a solution after given some constraints. We used the code gone over in the class as a base and worked with ways to generalize constraints to a solution. This did not prove to be fruitful but we were able to see how different aspects such as inital conditions and foralls can gum up the works for Z3 solutions. The constraint solution that we have satisfies the requirments for cutpoints by putting every while loops start it a cut point to generate a constraint. While this was created with the first problem in mind after testing it on a few other like problems it has show to generate reliable constraints with those problems.
