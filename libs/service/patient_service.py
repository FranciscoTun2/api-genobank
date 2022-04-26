import json
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
    if not patients:
      return []
    return patients

  def jsonify(self, patient):
    _json = patient.__dict__
    _json["created_at"] = str(_json["created_at"])
    _json["updated_at"] = str(_json["updated_at"])
    return _json


  