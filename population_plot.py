import pygal
import json
from country_codes import get_country_code
from pygal.maps.world import World

filename ='population_data2.json'
#load data into a list
with open(filename) as f:
    population_data = json.load(f)

cc_population = {}
for pop_dict in population_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

wm = World()
wm.title = 'World population in 2016, by country'
wm.add('2016', cc_population)

wm.render_to_file('world_population.svg')
