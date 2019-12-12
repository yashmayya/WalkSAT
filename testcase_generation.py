import os
import functools
import itertools
import random
import time

from walksat import GetClauseValue,Satisfies,FindVariablesInFalseClauses,FlipRandomVariables,SatCount,FlipVariables,FindMinConflictingVVars,ModifiedWalkSAT,PrintModel

start_time = time.time()

if not os.path.isdir('satisfiableinputs'):
	os.mkdir('satisfiableinputs')

n = 10	#Number of variables
variables = [i for i in range(1,n+1)]

ratios = [x/10 for x in range(5,81)]	#Generates list: 0.5,0.6,0.7,0.8,....,7.8,7.9,8.0

for ratio in ratios:
	i = 0
	m = int(n*ratio)	#Number of clauses
	
	while i < 20:	#Generate 20 problem instances for each ratio
		clauses = []
		j = 0
		
		while j<m:
			clause = random.sample(variables, 3)
			clause = sorted(clause)
			
			for k in range(3):
				if random.random()>=0.5:
					clause[k] = -1*clause[k]

			if clause not in clauses:
				clauses.append(clause)
				j = j+1

		model, ta = ModifiedWalkSAT(n,m,clauses,0.5,2000,1)


		if model:	#If clause is satisfiable

			filename = "satisfiableinputs/"+str(ratio)+"/input"+str(i)+".txt"
			
			i = i+1
			
			if not os.path.isdir(os.path.join("satisfiableinputs",str(ratio))):
				os.mkdir(os.path.join("satisfiableinputs",str(ratio)))

			with open(filename, "w") as fil:
				for clause in clauses:
					fil.write(" ".join(list(map(str, clause))))
					fil.write("\n")


print("--- %s seconds ---" % (time.time() - start_time))
