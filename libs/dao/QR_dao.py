from datetime import datetime

class QR:
  def __init__(self):
    self.table = "QRTable"
    self.taxonomy = None
    self.added = 0

  def validate_data(self, patient_data, name):
    validated = 0

    if patient_data[0].upper() != name.upper():
      validated += 1

    if patient_data[3].upper() != "N":
      validated += 1

    

    print(patient_data[8])
    
    if validated == 0:
      return True
    else:
      return False

    







  # def decodeCertificateUriData(self, data, taxnonomy):
  #   try:
  #     values = data.replace("%20", " ").split("%7C")
  #     print(len(values))
  #     if len(values) != 11:
  #       return False
  #     else:
  #       procedure = taxonomy.getProcedure(values[2])
  #       procedureResult = taxonomy.getProcedureResultByCode(procedure, values[3])

  #       platformData = {
  #         "txHash": values[10 + self.added],
  #         "signature": values[9 + self.added],
  #         "timeStamp": Date(values[8 + self.added]),
  #       }
  #     print (values)
  #   except:
  #     raise