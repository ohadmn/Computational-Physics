import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

# Globals 

# Grid size
GRID_SIZE = 101
# Time constant for color
TIME_CONSTANT = GRID_SIZE * GRID_SIZE // 6

# Grid to track anchored particles
grid = np.zeros((GRID_SIZE, GRID_SIZE), bool)

def add_particle(x, y, time=TIME_CONSTANT):
    """
    Adds a particle to the grid at position (x, y) and updates the plot.
    """
    grid[x, y] = True
    color = min(max(time / TIME_CONSTANT, 0), 1)  # Ensure color is within [0, 1]
    ax.plot(x, y, 's', color=str(color), markersize=5)

def generate_random_position(radius):
    """
    Generates x, y randomly on the circle with radius r+1.
    """
    theta = 2 * np.pi * np.random.random()
    x = int((radius + 1) * np.cos(theta) + GRID_SIZE // 2)
    y = int((radius + 1) * np.sin(theta) + GRID_SIZE // 2)
    return x, y

def calculate_distance(x, y):
    """
    Calculates the distance from the center of the grid to a position (x, y).
    """
    dx = x - GRID_SIZE // 2
    dy = y - GRID_SIZE // 2
    return np.sqrt(dx**2 + dy**2)

def random_walk_on_circle():
    """
    Performs the random walk for particles starting at the edge of a circle
    with an increasing radius until they stick to an anchored particle or an edge.
    """
    global radius
    max_radius = 0
    center = GRID_SIZE // 2, GRID_SIZE // 2
    time = 0

    while max_radius < GRID_SIZE // 2:
        time += 1
        x, y = generate_random_position(radius)
        while True:
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

            # Ensure the new position is within the grid boundaries
            if not (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE):
                break  # Discard particle if it goes out of bounds

            if calculate_distance(new_x, new_y) > 2 * radius:
                break  # Discard particle if it goes beyond 2r

            if grid[new_x, new_y]:
                add_particle(x, y, time=time)
                current_radius = calculate_distance(x, y)
                if current_radius > max_radius:
                    max_radius = current_radius
                break
            else:
                x, y = new_x, new_y

        radius = int(max_radius)
        if max_radius >= GRID_SIZE // 2:
            break

def main():
    global ax, radius
    radius = 0

    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.set_aspect('equal')

    # Initial particle position at the center
    initial_position = GRID_SIZE // 2, GRID_SIZE // 2
    add_particle(*initial_position)

    # Run the random walk simulation
    random_walk_on_circle()

    plt.show()

if __name__ == "__main__":
    main()
