# newton practice
import pytest 
import numpy as np 
import warnings

def fun(x):
    output = x**2 - 4
    return output

def newton_optimize(x, fun): 
    """
    This function takes derivates of a given global function wrt the input x, 
    and stops when the criteria of the abs difference between x and x2 is met.
    """
    epsilon = 0.1**10

    if not callable(fun):
        raise TypeError(f"The input for fun is not a callable function, but a {type(fun)}")
    if not isinstance(x, (int, float)):
        raise TypeError(f"The input for x is not a number, but a {type(fun)}")

    first_deriv = (fun(x+epsilon) - fun(x))/epsilon 
    x2 = x - x/first_deriv
    i = 0
    if first_deriv == 0:
        raise TypeError(f"First derivative is 0.") # I want it to stop if the first derivative is 0.

    while abs(x2 - x)>=0.01 and i <= 10000.0:
        x = x2 
        deriv = (fun(x+epsilon) - fun(x))/epsilon 
        if deriv == 0:
            warnings.warn(UserWarning(f"In the {i}th round, the derivative is 0."))
        if abs(deriv) <= 0.1**6: # an internal modification to avoid 0 being the denominator
            deriv += 0.1**6
        x2 = x - (x+0.1**6/deriv)
        i += 1
    print('the last round where the derivative is smaller than 0.1**6:', i)
    return x2

hahaha
