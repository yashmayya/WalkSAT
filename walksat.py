import functools
import itertools
import random

def GetClauseValue(model, clause):
	clauseval = []
	
	for i in range(len(clause)):
		if clause[i] < 0:	#Negative literal
			clauseval.append(1-model[abs(clause[i])-1])
		else:
			clauseval.append(model[abs(clause[i])-1])

	return functools.reduce(lambda a,b : a|b, clauseval)


def Satisfies(model, clauses):
	sat = 1

	for i in range(len(clauses)):
		sat = sat & GetClauseValue(model, clauses[i])

	return sat


def FindVariablesInFalseClauses(model, clauses):
	variables = set()

	for i in range(len(clauses)):
		if not Satisfies(model, [clauses[i]]):
			variables.update(clauses[i])

	variables = set(map(abs, variables))
	return variables


def FlipRandomVariables(model, s, v):
	li = list(s)

	if len(li) <= v:		#Flip all variables
		for i in range(len(li)):
			model[li[i]-1] = 1-model[li[i]-1]

	else:
		toflip = random.sample(li, v)
		for i in range(len(toflip)):
			model[toflip[i]-1] = 1-model[toflip[i]-1]


def SatCount(model, clauses):	#Returns number of satisfied clauses in model
	cnt = 0

	for i in range(len(clauses)):
		if Satisfies(model, [clauses[i]]):
			cnt = cnt+1

	return cnt


def FlipVariables(model, varbls):
	for i in varbls:
		model[i-1] = 1-model[i-1]


def FindMinConflictingVVars(model, clauses, v, n):
	varcombs = list(map(list, itertools.combinations([i for i in range(1, n+1)], v)))

	maxsat = 0
	maxsatidx = 0

	for i in range(len(varcombs)):
		FlipVariables(model, varcombs[i])
		
		satcnt = SatCount(model, clauses)
		if satcnt > maxsat:
			maxsat = satcnt
			maxsatidx = i

		FlipVariables(model, varcombs[i])

	FlipVariables(model, varcombs[maxsatidx])


def ModifiedWalkSAT(n,m,clauses,p,maxit,maxv):
	model = [random.choice([0,1]) for i in range(n)]
	totalassignments = 0

	for v in range(1,maxv+1):
		maxi = maxit
		while maxi > 0:
			maxi = maxi-1
			totalassignments = totalassignments + 1

			if Satisfies(model, clauses):
				return model, totalassignments

			s = FindVariablesInFalseClauses(model, clauses)

			if random.random() >= p:
				FlipRandomVariables(model, s, v)

			else:
				FindMinConflictingVVars(model, clauses, v, n)

	return [], totalassignments


def PrintModel(model):
	print("The variables to be assigned true are: (remaining to be assigned false)")
	for i in range(len(model)):
		if model[i]==1:
			print(i+1, end=" ")
	print()


def main():

	print("Input the set of clauses in DIMACS format")

	while True:
		comment = input()
		if comment[0]=='p':
			break

	n = int(comment.split()[2])	#Number of variables
	m = int(comment.split()[3]) #Number of clauses
	p = 0.5	#Probability of choosing random walk move

	clauses = []	#List of clauses

	for i in range(m):
		temp = []		
		clause = list(map(int, input().split()))
		temp = clause[:-1]
		clauses.append(temp)

	print("Input maximum number of assignments to be tried in each run: ")
	maxit = int(input())
	print("Input maximum number of variables to be simultaneously flipped: ")
	maxv = int(input())

	model, totalassignments = ModifiedWalkSAT(n,m,clauses,p,maxit, maxv)

	if model:
		print("Total assignments tried : {}".format(totalassignments))
		PrintModel(model)

	else:
		print("Couldn't find a satisfying assignment")


if __name__ == "__main__":
	main()