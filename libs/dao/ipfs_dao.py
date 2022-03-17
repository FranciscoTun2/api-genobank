import io
import json
import psycopg2
import requests
from settings import settings
# from libs import database_helpers as dbhelpers
# from libs import database

class ipfs:
  def __init__(self):
    super().__init__()

  def pin_ipfs(self, _data):
    try:
      image = io.BufferedReader(_data.file)
      # metadata = """{
      #     'name': 'ExampleNameOfDocument.pdf',
      #     'keyvalues': {
      #         'user': 'Lawyerfsdfijsdf001'
      #     }
      # }"""

      metadata = json.dumps({
        'name':'weather.jpg',
        'user':'0xa5461cbCf9c767264CC619bCF1AF3AaD083A5b22',
        'keyvalues':{
          'user':'0xa5461cbCf9c767264CC619bCF1AF3AaD083A5b22'
        }},
        separators=(',', ':')
      )
      myfile = {
            'file': image,
            'pinataMetadata': metadata,
            'pinataOptions': json.dumps({"cidVersion": '0'}, separators=(',', ':'))
        }
      _headers = {
            "pinata_api_key": settings.PINATA_API_KEY,
            "pinata_secret_api_key": settings.PINATA_API_SECRET
      }
      response = requests.post(settings.PINATA_HOST, files=myfile, headers=_headers)
      print(response.json)
      print(response.text)
      print(response.status_code)
      return response.json()
    except:
      raise
