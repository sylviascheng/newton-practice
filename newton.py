# newton practice
def fun(x):
    output = x**2 - 4
    return output

def newton_optimize(x):
    """
    This function takes derivates of a given global function wrt the input x, 
    and stops when the criteria of the abs difference between x and x2 is met.
    """
    epsilon = 0.1**5
    first_deriv = (fun(x + epsilon) - fun(x)) / epsilon
    x2 = x - x / first_deriv

    while abs(x2 - x) >= 0.01:
        x = x2
        deriv = (fun(x + epsilon) - fun(x)) / epsilon
        x2 = x - x / deriv
    return [x2, deriv]