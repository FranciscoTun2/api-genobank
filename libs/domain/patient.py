import json
import psycopg2
from libs import database_helpers as dbhelpers
from libs import database

class patient:
  def __init__(self,con):
    self.con = con
    self.table = "user"
  
  def create(self, data):
    print("patient domain", data)
    print("create", data)
    return data

  def validate(self, data):
    try:
      data = json.loads(data)
    except:
      raise Exception("Invalid json")
    if not data.get("email"):
      raise Exception("Email is required")
    if data.get("email") == "":
      raise Exception("Email is required")
    
    return data