import json
import psycopg2
from libs import database_helpers as dbhelpers
from libs import database

class patient_dao:
  def __init__(self,con):
    self.con = con
    self.table = "patients"
  
  def create(self, data):
    try:
      fields = f"""(name, idnumber, investigator, lab_logo, lab_name, test, test_result, test_date, email)"""
      sql = f"""INSERT INTO {self.table} {fields} VALUES ('{data["name"]}', '{data["idnumber"]}', '{data["labInvestigator"]}', '{data["labLogo"]}', '{data["labName"]}', '{data["test"]}', '{data["testresult"]}', '{data["testdate"]}','{data["email"]}')"""
      cur = self.con.cursor()
      cur.execute(sql)
      self.con.commit()
      cur.close()
      return cur
    except (psycopg2.DatabaseError) as error:
        self.con.rollback()
        cur.close()
        raise Exception(str(error))


  def all_patients(self):
    try:
      sql = f"""SELECT * FROM {self.table}"""
      cur = self.con.cursor()
      cur.execute(sql)
      rows = []
      for row in cur.fetchall():
        rows.append( dbhelpers.reg(cur, row) )
      cur.close()
      if rows:
        return rows[0]
      else:
        return False
    except (psycopg2.DatabaseError) as error:
      self.con.rollback()
      cur.close()
      raise Exception(str(error))


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

  # def create(self,data):
  #   sql = """ INSERT INTO documentos(id, title, file, created, reception_id, upload_by_id,hash,hash_file) VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5},'{6}' ,'{7}');"""
  #   cur = []
  #   try:
  #       cur = self.con.cursor()
  #       record= sql.format(int(data["id"]), data["title"], data["file"], data["created"],int(data["reception_id"]),int(data["upload_by_id"]),data["hash"],data["hash_file"])
  #       rows = cur.execute(record)
  #       self.con.commit()
  #       cur.close()
  #       return rows
  #   except (psycopg2.DatabaseError) as error:
  #       self.con.rollback()
  #       cur.close()
  #       raise Exception(str(error))