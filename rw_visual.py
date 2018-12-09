import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_pionts))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=15)
    plt.show()

    running = input("Make another walk? y/n: ")
    if running == 'n':
        break