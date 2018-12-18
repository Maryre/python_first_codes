import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print("Status code: ", req.status_code)

#store API response in a variable

response_dict = req.json()
print("Total Repositories: " , response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len((repo_dicts)))


#Examine the first repositoriy
# repo_dict = repo_dicts[0]
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    print("\nSelected information about first repository: ")
    print("Name:", repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Created: ', repo_dict['created_at'])
    print('Description:' , repo_dict['description'])
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

#Process results
# print(response_dict.keys())

#make visualization
my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most starred Python projects on Github'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')