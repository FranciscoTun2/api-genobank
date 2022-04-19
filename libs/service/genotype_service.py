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
    created = self.genotype.create(data)
    if not created:
      raise Exception("Error during genotype creation")
    return "ok"

  def create_nft(self, metadata):
    self.genotype.mint_nft(metadata)
    print(metadata)
    print("\n\n",metadata["wallet"])
    print("\n\n",metadata["wallet"][0])

    return False
    # created = self.genotype.create_nft(metadata)
    # return True if created else False