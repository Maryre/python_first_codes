import requests

url = 'http://api.open-notify.org/astros.json'
r = requests.get(url)
response_dict = r.json()
print("Status code: ", r.status_code)
# original data
print(response_dict)
# filter data
number = response_dict['number']
print("\nNumber of people in space now: " + str(number) + "\n")

print("the names of people in space now are: \n")
for keys in response_dict['people']:
    print( keys['name'])
    


