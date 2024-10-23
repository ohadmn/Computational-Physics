import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
h = 1e-6  # Time step
L = 1.0  # Length of the string in meters
v = 100.0  # Wave speed in m/s
d = 0.1  # Distance from the end where the string is struck
C = 1.0  # Amplitude of the initial velocity profile
sigma = 0.3  # Width of the initial velocity profile
N = 500  # Number of grid points
a = L / N  # Spacing between grid points

# Initial velocity profile function
def phi0(x):
    """
    Calculate the initial velocity profile of the string.
    """
    return C * x * (L - x) / L**2 * np.exp(- (x - d)**2 / (2 * sigma**2))

# Arrays to hold the displacement and velocity
fi = np.zeros(N+1, float)
x = np.linspace(0, L, N+1)
phi = phi0(x)

# Function to iterate the FTCS method
def iterate(fi, phi, dt=50e-3):
    """
    Perform iterations using the FTCS method to update displacement and velocity.
    """
    iterations = int(dt / h)
    for i in range(iterations):
        fi[1:N] += h * phi[1:N]
        phi[1:N] += h * v**2 / a**2 * (fi[2:N+1] + fi[0:N-1] - 2 * fi[1:N])
    return fi, phi

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot(x, fi * 2e3)
ax.set_ylim(-0.5, 0.5)  # Set the y-axis limits

# Animation update function
def update(frame):
    """
    Update the plot for each frame of the animation.
    """
    global fi, phi
    fi, phi = iterate(fi, phi, dt=50e-3/100)
    line.set_ydata(fi * 2e3)
    return line,

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), blit=True, interval=50)

plt.show()
