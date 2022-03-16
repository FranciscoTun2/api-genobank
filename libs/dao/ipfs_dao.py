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
      print("\n\nIT WORKS!!!\n\n")
      # print("\ndata\n",_data.file)
      # print("\ndata fp\n",data.rb)


      # myfile = {'file' :  open('download.png','rb')}
      myfile = {"file":open('download.png','rb')}
      print("\n\n MYfile:\n",myfile,"\n\n")

      _headers = {
            "pinata_api_key": settings.PINATA_API_KEY,
            "pinata_secret_api_key": settings.PINATA_API_SECRET
      }
      # body = json.dumps(data)
      # body = _data
      # print("\n\n",body,"\n\n")
      response = requests.post(settings.PINATA_HOST, data = myfile, headers = _headers)
      print("\n\n",response.json)
      print(response.text)
      print(response.status_code,"\n\n")

    except:
      raise
