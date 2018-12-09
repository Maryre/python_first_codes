import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_pionts))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=10)
    #emphsize the first and last points
    plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #remove the axes
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    #set the size of the plotting window
    #plt.figure(dpi=128, figsize=(10,6))
    plt.show()

    running = input("Make another walk? y/n: ")
    if running == 'n':
        break