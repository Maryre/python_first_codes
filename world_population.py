import json
from country_codes import get_country_code

filename ='population_data2.json'

#load data into a list
with open(filename) as f:
    population_data = json.load(f)

#print the data for 2016
for pop_dict in population_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            print(code+ ': ' + str(population))
        else:
            print('ERROR - ' + country_name)
    # else:
    #     print("no such data")