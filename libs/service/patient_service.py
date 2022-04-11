from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.dao import patient_dao

class patient_service:
  def __init__(self, _patient):
    if not isinstance(_patient, patient_dao.patient_dao):
      raise DomainInjectionError.DomainInjectionError("patient_service", "patient")
    self.patient = _patient
    self.encryption = Encryption.Encryption()

  def create(self, data):
    created = self.patient.create(data)
    if not created:
      raise Exception("Error during patient creation")
    return "ok"

  def all_patients(self):
    patients = self.patient.all_patients()
    return patients

  