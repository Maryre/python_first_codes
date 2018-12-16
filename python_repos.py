import requests

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
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

#Process results
print(response_dict.keys())