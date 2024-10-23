def f(x):
    """
    Evaluates f(x) for any given value of x.

    Arguments:
    x (float): The value we want to evaluate f(x) for.

    Returns:
    float: The value of f(x) for a given value of x.
    """
    return x**4-2*x+1
    
def simpsons_rule(a, b, n):
    """
    Calculates the approximation of an integral between the limits a to b, using Simpson's rule over n subintervals.

    Arguments:
    a (float): The lower limit of the main interval.
    b (float): The upper limit of the main interval.
    n (int): The number of subintervals.
    h (float): The width of a single subinterval.

    Returns:
    integral (float): The approximate integral from a to b of f(x) using Simpson's rule with N subintervals
    """
    h = (b-a)/n # The width of a single subinterval
    integral = f(a) + f(b) # Including the values of the limits in the integral summation
    for i in range(1, n):
        x_i = a + i*h # The evaluation points in which f(x) will be evaluated.
        if i%2 == 0:
            integral += 2 * f(x_i) # For even indices, multiply by a factor of 2 because these are "junction points" - the endpoints of a single parabolic segment
        else:
            integral += 4 * f(x_i) # For odd indices, multiply by a factor of 4 because these are midpoints
    
    integral *= h/3 # Multiplies by factor 1/3 due to "Simpson's 1/3 rule"
    
    return integral

def fractional_error_calc(calculated_value):
    """
    Calculates the fractional error between the approximate integral's result and the true value of the integral.

    Arguments:
    calculated_value (float): The value obtained from calculations.

    Returns:
    fractional_error (float): The fractional error.
    """
    true_value = 4.4 # The known value to compare against
    fractional_error = abs(calculated_value - true_value) / abs(true_value)
    return fractional_error
    
def main():
    # Constants
    N = 10 # Num of subintervals
    a = 0.0 # Lower limit
    b = 2.0 # Upper limit
        
    # Section A
    res = simpsons_rule(a, b, N)
    print(f"A. The approximate integral from {a} to {b} of f(x) using Simpson's rule with {N} subintervals is {res}.")

    # Section B
    error = fractional_error_calc(res)
    print(f"B. The fractional error is: {error}.")

    # Section C
    N_100 = 100 # 100 subintervals
    N_1000 = 1000 # 100 subintervals
    
    res_100 = simpsons_rule(a, b, N_100)
    error_100 = fractional_error_calc(res_100)

    res_1000 = simpsons_rule(a, b, N_1000)
    error_1000 = fractional_error_calc(res_1000)

    print(f"C. The approximate integral from {a} to {b} of f(x) using Simpson's rule with {N_100} subintervals is {res_100}.\nThe fractional error is: {error_100}.")
    print(f"The approximate integral from {a} to {b} of f(x) using Simpson's rule with {N_1000} subintervals is {res_1000}.\nThe fractional error is: {error_1000}.")

    
if __name__=='__main__':
    main()