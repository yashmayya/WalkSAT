# WalkSAT

A modified implementation of the classic local search algorithm WalkSAT for the 3SAT problem. 

Classic WalkSAT takes parameters **n** (number of variables), **m** (number of clauses), **C** (set of clauses in DIMACS format), **p** (probability of flipping) and **maxit** (maximum number of assignments to be tried in each run)

This implementation takes an additional parameter **maxv** (maximum number of variables to be simultaneously flipped).

WalkSAT is run maxv number of times (with the parameter v (number of variables to be flipped) varying from 1 to maxv).

Essentially, we find the set S of variables that are present in the clauses that are FALSE. Randomly select v variables from the set S, and flip their values with probability p. (If set S contains less than v variables, then flip all the variables in S with probability p.) Otherwise, with probability (1 - p) flip v variables such that the number of FALSE clauses are minimized.

The **pseudo-code** for the algorithm is:

```
ModifiedWalkSAT
Require : n,m: The number of variables and clauses.
Require: C: The set of clauses (in DIMACS format).
Require: p: The probability of flipping.
Require: maxit: Maximum number of assigments to be tried in each run.
Require: maxv: Maximum number of variables to be simultaneously flipped.
1: M  = Random(domain= [0, 1], length= n)
2: v = 0
3: while v < maxv do
4:    v = v + 1
5:    while maxit > 0 do
6:      maxit = maxit - 1
7:      if Satisfies(M,C) then
8:        return M
9:      end if
10:     S = FindVariablesInFalseClauses(C)
11:     if Random() >= p then
12:       M = FlipVariables(M, S, v)
13:     else
14:       M = FindMinConflictingVVars(M, C, v)
15:     end if
16:   end while
17: end while
18: return Failure
```

### Creating test benchmarks

Running **testcase_generation.py** creates 20 WalkSAT problems randomly for m/n ratios of 0.5,0.6,0.7....7.8,7.9,8.0 for fixed n value (10).

### Performance graph

Running **performance_benchmark.py** runs the modified WalkSAT implementation for each of the randomly generated WalkSAT problems and calculates average running time for each m/n ratio and plots it in a graph (using **matplotlib**)
