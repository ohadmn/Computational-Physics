from numpy import array, arange, pi, sin, cos, sqrt, linspace
from matplotlib import pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
R = 0.08  # radius of the cannonball (m)
theta_0 = 30 * pi / 180  # launch angle converted to radians
v_0 = 100  # initial velocity (m/s)
rho = 1.22  # air density (kg/m^3)
C = 0.47  # drag coefficient
m = 1  # mass of the cannonball (kg)

t_0 = 0  # start time (s)
t_f = 7  # end time (s)
N = 10000  # number of time points
h = (t_f - t_0) / N  # step size (s)

def drag_coefficient(m):
    """
    Calculates the drag coefficient used for air resistance calculations, given the mass of the projectile.

    Arguments:
    m (float): Mass of the projectile in kilograms.

    Returns:
    float: The computed drag coefficient factor used in the drag force formula.
    """

    return (pi * R**2 * rho * C) / (2 * m)


def equations_of_motion(r, t, m):
    """
    Calculates the derivatives for the system of equations governing projectile motion under gravity and air resistance.
    
    Arguments:
    r (array): Current state vector [x, vx, y, vy] where x and y are positions and vx and vy are velocities.
    t (float): Current time (not used in this function, but typically required by ODE solvers).
    m (float): Mass of the projectile in kilograms.
    
    Returns:
    array: Derivatives [dx/dt, dvx/dt, dy/dt, dvy/dt] for use in numerical integration.
    """

    vx, vy = r[1], r[3]
    v = sqrt(vx**2 + vy**2)
    Fx = -drag_coefficient(m) * vx * v
    Fy = -g - drag_coefficient(m) * vy * v
    return array([vx, Fx, vy, Fy], float)

def trajectory(m):
    """
    Computes the trajectory of the projectile using the fourth-order Runge-Kutta method to solve the differential equations.
    
    Arguments:
    m (float): Mass of the projectile in kilograms.
    
    Returns:
    tuple:
        array: x-coordinates of the projectile over time.
        array: y-coordinates of the projectile over time.
    """

    # Initial conditions
    r = array([0, v_0 * cos(theta_0), 0, v_0 * sin(theta_0)], float)
    xpoints, ypoints = [], []

    for t in arange(t_0, t_f, h):
        xpoints.append(r[0])
        ypoints.append(r[2])
        k1 = h * equations_of_motion(r, t, m)
        k2 = h * equations_of_motion(r + 0.5 * k1, t + 0.5 * h, m)
        k3 = h * equations_of_motion(r + 0.5 * k2, t + 0.5 * h, m)
        k4 = h * equations_of_motion(r + k3, t + h, m)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return array(xpoints), array(ypoints)

def main():
    #Secion B.
    # Plot the trajectory of the cannonball
    x_points, y_points = trajectory(m)
    plt.plot(x_points, y_points)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Trajectory of the Cannonball')
    plt.grid(True)
    plt.show()

    #Section C.
    # Different masses
    masses = linspace(0.5, 2, 10)  # From 0.5 to 2 kg
    distances = []
    
    for mass in masses:
        x, y = trajectory(mass)
        distances.append(x[-1])
    
    # Plot distance traveled as a function of mass of the cannonball
    plt.figure(figsize=(10, 6))
    plt.plot(masses, distances, '-o')
    plt.xlabel('Mass (kg)')
    plt.ylabel('Distance Traveled (m)')
    plt.title('Distance Traveled as a Function of the Mass of the Cannonball')
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    main()