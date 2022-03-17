from email import header
import json
import requests
import json

image = open('sitegenobank.png', 'rb')
metadata = {"name": "MyExampleDOcument","keyvalues": {"Company": "Pnnatas And Co"}}

_file = {
    'file': image,
    'pinataMetadata': metadata
    }


_headers = {
    "pinata_api_key": "ba65da047212926c9ee4",
    "pinata_secret_api_key": "3897644a77bf3ea3836a17fa1bed1c8897f95e5f148be0728e2f73c48aa7baec",
    "Content-Type'" : "application/json"
}
try:
    response = requests.post("https://api.pinata.cloud/pinning/pinFileToIPFS", files=_file, headers=_headers)

    print(response.json)
    print(response.text)
    print(response.status_code)
except:
    raise
