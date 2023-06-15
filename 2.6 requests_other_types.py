import requests

# You can create your own requests!
r = requests.request("CREATE", "https://run.mocky.io/v3/f545c75d-4a62-450d-b9fd-bfeb9ae0a583")

print(r.text)
print(r.headers)
