import json


filename ='population_data2.json'

#load data into a list
with open(filename) as f:
    population_data = json.load(f)

#print the data for 2016
for pop_dict in population_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ': ' + str(population))
    # else:
    #     print("no such data")