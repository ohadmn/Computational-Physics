import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint


#Globals

# Grid size
GRID_SIZE = 201
# Time constant for color
TIME_CONSTANT = GRID_SIZE * GRID_SIZE // 6

# Grid to track anchored particles
grid = np.zeros((GRID_SIZE, GRID_SIZE), bool)

def add_particle(x, y, time=TIME_CONSTANT):
    """
    Adds a particle to the grid at position (x, y) and updates the plot.
    """
    grid[x, y] = True
    color = time / TIME_CONSTANT  # Fixed color for all particles
    ax.plot(x, y, 's', color=str(color), markersize=5)

def generate_random_position(radius=0):
    """
    Generates x, y randomly on the circle with radius r+1.
    """
    theta = 2 * np.pi * np.random.random()
    x = int((radius + 1) * np.cos(theta) + GRID_SIZE // 2)
    y = int((radius + 1) * np.sin(theta) + GRID_SIZE // 2)
    return x, y

def calculate_distance(x, y):
    """
    Calculates the Euclidean distance from the center of the grid to the position (x, y).
    """
    dx = x - GRID_SIZE // 2
    dy = y - GRID_SIZE // 2
    distance = np.sqrt(dx**2 + dy**2)
    return distance

def random_walk_on_circle():
    """
    Performs the random walk for particles starting on the circumference of a circle.
    The particle moves randomly until it sticks to another anchored particle.
    """
    # Initial particle position at the center
    initial_position = GRID_SIZE // 2, GRID_SIZE // 2
    add_particle(*initial_position)

    time = 0
    radius = 1
    while radius * 2 < GRID_SIZE // 2:
        time += 1
        x, y = generate_random_position(radius)
        distance = 0
        while distance <= 2 * radius:
            direction = randint(4)
            new_x, new_y = x, y
            if direction == 0:  # move up
                new_x += 1
            elif direction == 1:  # move down
                new_x -= 1
            elif direction == 2:  # move right
                new_y += 1
            elif direction == 3:  # move left
                new_y -= 1

            if grid[new_x, new_y]:
                add_particle(x, y, time=time)
                if radius < distance:
                    radius = int(distance)
                break
            else:
                x, y = new_x, new_y
            distance = calculate_distance(x, y)

def main():
    """
    Main function to set up the plot and run the optimized diffusion-limited aggregation simulation.
    """
    global ax
    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.set_aspect('equal')

    # Run the random walk simulation
    random_walk_on_circle()

    # Show the final result
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
