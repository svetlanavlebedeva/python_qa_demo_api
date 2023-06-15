import requests

session = requests.Session()

session.auth = ('user', 'password')

response = session.get('https://httpbin.org/basic-auth/user/password')
response2 = session.get('https://httpbin.org/basic-auth/user/password')

print(response.text)
print(response2.text)
