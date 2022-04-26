from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.dao import genotype_dao

class genotype_service:
  def __init__(self, _genotype):
    if not isinstance(_genotype, genotype_dao.genotype_dao):
      raise DomainInjectionError.DomainInjectionError("genotype_service", "genotype")
    self.genotype = _genotype
    self.encryption = Encryption.Encryption()

  def create(self, data, file):
    file_name = self.genotype.save_file(file)
    if not file_name:
      raise Exception("File not saved")
    data["file"] = file_name
    print("\ndata\n", data)
    created = self.genotype.create(data)
    if not created:
      raise Exception("Error during genotype creation")
    return "ok"

  def create_nft(self, metadata):
    created = self.genotype.mint_nft(metadata)
    if not created:
      raise Exception("Error during genotype creation")
    return created

  def generate_token_id(self, token):
    token_id = self.genotype.generate_token_id(token)
    if not token_id:
      raise Exception("Error during genotype creation")
    return token_id