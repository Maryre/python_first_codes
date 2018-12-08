import matplotlib.pyplot as plt

#S = size of the plot
#plt.scatter(2, 4, s=200)
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1,1001))
y_values= [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c=(0, 1, 0.8), edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.magma, edgecolor='none', s=40)

#set chart title and lable
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Square of Value", fontsize=15)

#set the range for each axis
plt.axis([0, 1100, 0, 1100000])
#set size of thick lables
#plt.tick_params(axis='both', which='major', labelsize=15)
#plt.show()

plt.savefig('Squateplot.png', bbox_inches='tight')