import json
import uuid
import psycopg2
from libs import database_helpers as dbhelpers
from libs import database

class genotype_dao:
  def __init__(self,con):
    self.con = con
    self.table = "genoma"

  def create(self, data):
    try:
      fields = f"""(jsondata, consent, test_type, file_stored)"""
      _json = json.dumps(data)
      sql = f"""INSERT INTO {self.table} {fields} VALUES ('{_json}', '{json.dumps(data["agreements"])}', '{data["genetic_test"]}', '{data["file"]}')"""
      cur = self.con.cursor()
      cur.execute(sql)
      self.con.commit()
      cur.close()
      return cur
    except (psycopg2.DatabaseError) as error:
      self.con.rollback()
      cur.close()
      raise Exception(str(error))

  def save_file(self, file):
    content_file = str(file.file.read().decode("utf-8"))
    file_name = str(uuid.uuid4())
    with open(f"files/genotypes/{file_name}.txt", "w") as f:
      f.write(content_file)
    return file_name
