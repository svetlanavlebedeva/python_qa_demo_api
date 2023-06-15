import requests

query = {'lang': 'eng',
         'id': 18}

r = requests.get('https://meowfacts.herokuapp.com/', params=query)

print(r.json())
