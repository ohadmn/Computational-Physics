# imports
from numpy import array, empty
import math

def gaussian_elimination(A, v):
    """
    Solves a system of equations using Gaussian elimination and back substitution.

    Arguments:
    A (array): A system of equations that includes the coefficients of the different junctions.
    v (array):

    Returns:
    x (array): An array that contains the float values of the voltages of the junctions, from V1 to V4.
    """
    N = len(v)
    
    # Gaussian elimination
    for m in range(N):
        # Divide by the diagonal element of the array
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Subtract from the lower rows
        for i in range(m+1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    # Backsubstitution to solve for the voltages' equations
    x = empty(N, float)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i] * x[i]

    return x 
    
def main():
    # Constants
    A = array([[4, -1, -1, -1],
               [-1, 4, -1, -1],
               [-1, -1, 4, -1],
               [-1, -1, -1, 4]], float) # The four resulting equations of the four junctions.
    v = array([5, 0, 0, 0], float) # V+ is 5 volts, and the other junctions are 0.
    voltages = gaussian_elimination(A, v)
    print("B.")
    for i in range(4):
        print(f"Voltage of junction V{i+1} = {math.ceil(voltages[i])} Volt") # Prints the rounded (up) value of each junction.
    
if __name__=='__main__':
    main()