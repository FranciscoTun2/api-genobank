import json
import psycopg2
from libs import database_helpers as dbhelpers
from libs import database

class genotype_dao:
  def __init__(self,con):
    self.con = con
    self.table = "genotypes"

  def create(self, data):
    try:
      fields = f"""(jsondata, consent, test_type, genotype)"""
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
