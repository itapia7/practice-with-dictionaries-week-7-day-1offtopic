#working with api's and dictionaries

import requests
import json
response = requests.get("https://randomuser.me/api")

#print(response.json())

title = response.json()['results'][0]['name']['first']
print(title)
gender = response.json()['results'][0]['gender']
print(gender)
lastn = response.json()['results'][0]['name']['last']
print(lastn)
streetn = response.json()['results'][0]['location']['street']['name']
print(streetn)
city = response.json()['results'][0]['location']['city']
state = response.json()['results'][0]['location']['state']
country = response.json()['results'][0]['location']['country']
postalcode = response.json()['results'][0]['location']['postcode']
print(city)
print(state)
print(country)
print(postalcode)
email = response.json()['results'][0]['email']
print(email)
user = response.json()['results'][0]['login']['username']
print(user)