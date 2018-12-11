import pygal
from die import Die

#create a D6 and a D10
die_1 = Die(8)
die_2 = Die(8)

#Make some roles and store result
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the result

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)



#Visualize the results
hist = pygal.Bar()
hist._title = 'Results of rolling two D8 dices 1000000 times'
hist.x_labels = [str(x) for x in range(2, max_results+1)]
hist._x_title = "Result"
hist._y_title = 'Frequenty of results'

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual8.svg')