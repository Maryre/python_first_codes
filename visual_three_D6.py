import pygal
from die import Die

#create a D6 and a D10
die_1 = Die()
die_2 = Die()
die_3 = Die()

#Make some roles and store result
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyze the result

frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)



#Visualize the results
hist = pygal.Bar()
hist._title = 'Results of rolling three D6 dices 50000 times'
hist.x_labels = [str(x) for x in range(3, max_results+1)]
hist._x_title = "Result"
hist._y_title = 'Frequenty of results'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_visual6_3times.svg')