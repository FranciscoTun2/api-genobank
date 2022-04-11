from email import header
import json
import requests
import json

image = open('sitegenobank.png', 'rb')
# metadata = {
#     "name": 'ExampleNameOfDocument.pdf',
#     "keyvalues": {
#         "LawyerName": 'Lawyer001',
#         "ClientID": 'Client002',
#         "ChargeCode": 'Charge003'
#         "Cost": "100.00"
#     }
# }

metadata = {
    'name': 'ExampleNameOfDocument.pdf',
    'keyvalues': {
        'user': 'Lawyerfsdfijsdf001'
    }
}

_file = {
    'file': image,
    'pinataMetadata': metadata,
    'pinataOptions': {"cidVersion": 0}
    }


_headers = {
    "pinata_api_key": "ba65da047212926c9ee4",
    "pinata_secret_api_key": "3897644a77bf3ea3836a17fa1bed1c8897f95e5f148be0728e2f73c48aa7baec",
    "Content-Type'" : "application/json"
}
try:
    response = requests.post("https://api.pinata.cloud/pinning/pinFileToIPFS", files=_file, headers=_headers)
except:
    raise
