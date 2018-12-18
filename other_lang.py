import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
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
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)


#make visualization
my_style = LS('#334422', base_style=LCS)
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
chart.add('', plot_dicts)
chart.render_to_file('java_repos.svg')