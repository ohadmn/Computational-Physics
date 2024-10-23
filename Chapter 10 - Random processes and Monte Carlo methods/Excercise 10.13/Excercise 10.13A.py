import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint


# Globals

# Grid size
GRID_SIZE = 101
# Time constant for color
TIME_CONSTANT = GRID_SIZE * GRID_SIZE // 6

# Initial particle position at the center
INITIAL_POS = GRID_SIZE // 2, GRID_SIZE // 2
# Grid to track anchored particles
grid = np.zeros((GRID_SIZE, GRID_SIZE), bool)

def add_particle(x, y, time=0):
    """
    Adds a particle to the grid at position (x, y) and updates the plot.
    The color of the particle is determined based on the time it was added.
    """
    grid[x, y] = True
    color = time / TIME_CONSTANT  #Color based on time
    color = max(0, min(1, color))  # Ensure color is within [0, 1]
    ax.plot(x, y, 's', color=str(color), markersize=5)

def random_walk():
    """
    Performs the random walk for a particle starting at the center of the grid.
    The particle moves randomly until it sticks to an edge or an anchored particle.
    """
    time = 0
    while not grid[INITIAL_POS]:
        time += 1
        x, y = INITIAL_POS
        while True:
            direction = randint(4)
            if direction == 0:  # move up
                if x == GRID_SIZE - 1 or grid[x + 1, y]:
                    add_particle(x, y, time=time)
                    break
                else:
                    x += 1
            elif direction == 1:  # move down
                if x == 0 or grid[x - 1, y]:
                    add_particle(x, y, time=time)
                    break
                else:
                    x -= 1
            elif direction == 2:  # move right
                if y == GRID_SIZE - 1 or grid[x, y + 1]:
                    add_particle(x, y, time=time)
                    break
                else:
                    y += 1
            elif direction == 3:  # move left
                if y == 0 or grid[x, y - 1]:
                    add_particle(x, y, time=time)
                    break
                else:
                    y -= 1

def main():
    global ax
    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    
    # Run the random walk simulation
    random_walk()

    plt.show()

if __name__ == "__main__":
    main()
