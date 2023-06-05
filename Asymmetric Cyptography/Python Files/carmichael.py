from trial_division import trialDivision
import numpy as np

def korselt(factors):
    #Checks if the factors satisfies the divisibility of Korselt's criterion
    #param: factors(int[]): the factors to be checked
    #returns True if all satisfy the criterion
    N = np.prod(factors)
    for factor in factors:
        if (N - 1) % (factor - 1) != 0:
            return False
    return True
