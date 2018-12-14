import pygal
import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle

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

#Group countries into 3 population levels:
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop <  10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

#see how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World population in 2016, by country'
#wm.add('2016', cc_population)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)


wm.render_to_file('world_population.svg')
