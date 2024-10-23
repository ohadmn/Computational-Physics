#imports
from numpy import exp, array, dot

# Constants
V_p = 5 # V_plus ; Volts
R1 = 1e3 # R_1 ; Ohm
R2 = 4e3 # R_2 ; Ohm
R3 = 3e3 # R_3 ; Ohm
R4 = 2e3 # R_4 ; Ohm
I0 = 3e-9 # I_0 ; Amper
V_T = 0.05 # V_T ; Volts
target = 1.0e-3  # Volts

def f(arr):
    """
    Calculates the system of equations representing the circuit.

    Arguments:
    arr (array): An array containing the intial guesses for the voltages of the junctions V1 and V2.

    Returns:
    array: An array containing the equations representing the circuit.
    """
    return array([(arr[0] - V_p) / R1 + arr[0] / R2 + I0 * (exp((arr[0] - arr[1]) / V_T) - 1),
                (V_p - arr[1]) / R3 - arr[1] / R4 + I0 * (exp((arr[0] - arr[1]) / V_T) - 1)],float)

def grad_f(arr):
    """
    Calculates the Jacobian matrix of the system of equations.

    Arguments:
    arr (array): An array containing the intial guesses of the voltages of the junctions V1 and V2.

    Returns:
    array: The Jacobian matrix of the system of equations.
    """
    return array([[ 1 / R1 + 1 / R2 + I0 / V_T * exp((arr[0] - arr[1]) / V_T), -I0 / V_T * exp((arr[0] - arr[1]) / V_T)],
                [I0 / V_T * exp((arr[0] - arr[1]) / V_T), -1 / R3 - 1 / R4 - I0 / V_T * exp((arr[0] - arr[1]) / V_T)]], float)


def inverse_matrix_2x2(arr):
    """
    Calculates the inverse of a 2x2 matrix.

    Arguments:
    arr (array): A 2x2 matrix.

    Returns:
    array: The inverse of the input matrix.
    """
    return 1 / (arr[0, 0] * arr[1, 1] - arr[0, 1] * arr[1, 0]) * array([[arr[1, 1], -arr[0, 1]], [-arr[1, 0], arr[0, 0]]], float)

def main():
    x1 = array([3, 2.4], float) # Initial guess for V1 and V2
    delta_x = dot(inverse_matrix_2x2(grad_f(x1)),f(x1)) # Delta x according to equation (6.108) is the inverse of the Jacobian matrix multipied by f(x)
    while abs(delta_x[0]) > target or abs(delta_x[1]) > target: # Iterating over the values of V1 and V2 untill they are within the range of the defined target value.
        delta_x = dot(inverse_matrix_2x2(grad_f(x1)), f(x1)) # Calculate the change in the voltages using Newton's method.
        x1 -= delta_x
    
    print('V1 = ', x1[0])
    print('V2 = ', x1[1])
    
if __name__=='__main__':
    main()