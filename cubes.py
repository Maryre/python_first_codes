import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.spring,
            edgecolor='none', s=50)

#set chart title and lable
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Cubes of Value", fontsize=15)


#plt.tick_params(axis='both', labelsize=15)
plt.axis([0, 5100, 0, 5100**3])
plt.show()
#plt.savefig('cubesplot.png', bbox_inches='tight')