import os
import math
import matplotlib.pyplot as plt

from assignment2 import GetClauseValue,Satisfies,FindVariablesInFalseClauses,FlipRandomVariables,SatCount,FlipVariables,FindMinConflictingVVars,ModifiedWalkSAT,PrintModel

ratios = [x/10 for x in range(5,81)]	#To be plotted on x axis
runtime = []	#To be plotted on y axis


for ratio in ratios:
	totaliterations = 0

	for i in range(20):	#20 files per ratio
		filename = os.path.join("satisfiableinputs", str(ratio), "input{}.txt".format(str(i)))
		clauses = []

		with open(filename, "r") as fil:
			for line in fil:
				clauses.append([int(x) for x in line.split()])

		n = 10
		m = int(ratio*n)

		model, iterations = ModifiedWalkSAT(n,m,clauses,0.5,2000,1)

		totaliterations = totaliterations + iterations

	runtime.append(math.log(totaliterations/20))

plt.plot(ratios, runtime)
plt.xlabel("Clause symbol ratio m/n")
plt.ylabel("Log of mean runtime")
plt.show()