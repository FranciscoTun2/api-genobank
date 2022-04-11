from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.dao import genotype_dao

class genotype_service:
  def __init__(self, _genotype):
    if not isinstance(_genotype, genotype_dao.genotype_dao):
      raise DomainInjectionError.DomainInjectionError("genotype_service", "genotype")
    self.genotype = _genotype
    self.encryption = Encryption.Encryption()

  def create(self, data):
    if "file" not in data:
      data["file"] = "File not found"
    
    created = self.genotype.create(data)
    if not created:
      raise Exception("Error during genotype creation")
    return "ok"