import requests

from test_data import DOG_FILE_PATH

headers = {'api_key': 'special-key'}

json = {
    "name": "doggie",
    "photoUrls": [
        "https://cdn2.thedogapi.com/images/njDSq3gRF.jpg"
    ]
}

r = requests.post(url='https://petstore.swagger.io/v2/pet',
                  headers=headers,
                  json=json)

print(r.json())

dog_id = r.json()['id']

with open(DOG_FILE_PATH, 'rb') as f:
    files = {'file': f,
             'type': 'image/jpeg'}

    file_headers = {'api_key': 'special-key'}

    r_upload = requests.post(url='https://petstore.swagger.io/v2/pet/{}/uploadImage'.format(dog_id),
                             headers=file_headers,
                             files=files)
    print(r_upload.json())
