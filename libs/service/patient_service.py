from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.domain import patient

class patient_service:
  def __init__(self, _patient):
    if not isinstance(_patient, patient.patient):
      raise DomainInjectionError.DomainInjectionError("patient_service", "patient")
    self.patient = _patient
    self.encryption = Encryption.Encryption()

  def create(self, data):
    created = self.patient.create(data)
    if not created:
      raise Exception("Error during patient creation")

  