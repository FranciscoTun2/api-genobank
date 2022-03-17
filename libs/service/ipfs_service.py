from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.dao import ipfs_dao
class ipfs_service:
    def __init__(self, _ipfs):
      if not isinstance(_ipfs, ipfs_dao.ipfs):
        raise DomainInjectionError.DomainInjectionError("ipfs_service", "ipfs")
      self.ipfs = _ipfs
      self.encryption = Encryption.Encryption()

    def pin_ipfs(self, data):
      ipfss = self.ipfs.pin_ipfs(data)
      return ipfss