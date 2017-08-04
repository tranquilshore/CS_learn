#Problem
'''
Problem:
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
(allowing repetitions and different arrangements).

Solution:
first of all, we decide a state for the given problem. 
take a parameter n to decide state as it can uniquely identify any subproblem

Let us assume that we know the result for n = 1,2,3,4,5,6.
Now, we wish to know the result of the state (n = 7). See, we can only add 1, 3 and 5. Now we can get a sum total of 7 by the following 3 ways:
1.  Adding 1 to all possible combinations of state (n = 6)
2.  Adding 3 to all possible combinations of state (n = 4)
3.  Adding 5 to all possible combinations of state (n = 2)

Therefore, we can say that result for
state(7) = state (6) + state (4) + state (2)
or
state(7) = state (7-1) + state (7-3) + state (7-5)

In general,
state(n) = state(n-1) + state(n-3) + state(n-5)
'''
#recursive
def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return solve(n-1) + solve(n-3) + solve(n-5)
print solve(6)

#memoization
lookup = [None]*101
def m_solve(n, lookup):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if lookup[n] != None:
        return lookup[n]
    lookup[n] = m_solve(n-1, lookup) + m_solve(n-3,lookup) + m_solve(n-5, lookup)
    return lookup[n]
print m_solve(6, lookup)

