import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, c='green', s=15)
    plt.show()

    running = input("Make another walk? y/n: ")
    if running == 'n':
        break