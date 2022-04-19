from web3 import Web3, HTTPProvider
# from web3.middleware import geth_poa_middleware
import json
import uuid
import psycopg2
from libs import database_helpers as dbhelpers
from libs import database
from settings import settings

class genotype_dao:
  def __init__(self,con):
    self.w3 = Web3(HTTPProvider(settings.PROVIDER))
    # self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    self.SM_JSONINTERFACE = self.load_smart_contract(settings.ABI_SM_PATH)
    self.con = con
    self.table = "genoma"

  def load_smart_contract(self,path):
        solcOutput = {}
        try:
            with open(path) as inFile:
                solcOutput = json.load(inFile)
        except Exception as e:
            print(f"ERROR: Could not load file {path}: {e}")
        return solcOutput

  # call smar contract metrhod using address and jsonInterface
  def mint_nft(self, metadata):
    account = self.w3.eth.account.privateKeyToAccount(settings.ROOT_KEY)
    print("\n\n",account.address)
    wallet = metadata["wallet"]
    contract = self.w3.eth.contract(address=settings.SMART_CONTRACT, abi=self.SM_JSONINTERFACE['abi'])
    print("All functions\n",contract.all_functions())
    id_address = int(account.address, 16)


    # tx_hash = contract.functions.mint(id_address, metadata["wallet"], 'ACTIVE').transact()
    tx_hash = contract.caller().mint(id_address, wallet, 'ACTIVE').call({'from': '0x1FCe7a83BbE1Cd899AF95A1Dda5299CA06438bA8'})
    print("tx hash\n",tx_hash)


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
