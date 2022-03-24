from datetime import datetime
from numpy import double

class QR:
  def __init__(self):
    self.table = "QRTable"
    self.taxonomy = None
    self.added = 0

  def validate_data(self, patient_data, name):
    valString = ""
    validated = 0
    now_timestamp = float(datetime.now().timestamp())
    c_timestamp = int(patient_data[8])
    c_timestamp = float(c_timestamp/1000)

    life_time = now_timestamp - c_timestamp
    life_timer_h = life_time / (3600)

    valString+= "validating if name:\n" + name + "\nis equal to:\n" + patient_data[0].upper() + "\n"
    if patient_data[0].upper() != name.upper():
      validated += 1

    valString+= "validating test type 1) Polymerase, 2) Antigen:\n" + str(patient_data[2]) + "\n"
    if int(patient_data[2]) == 1:
      valString+= "Polymerase\n"
      valString+= "Life time is over 48 hours\n"+ str(life_timer_h) + "\n"
      if life_timer_h > 48:
        validated += 1
    if int(patient_data[2]) == 2:
      valString+= "Antigen\n"
      valString+= "Life time is over 24 hours\n"+ str(life_timer_h) + "\n"
      if life_timer_h > 24:
        validated += 1

    if patient_data[3].upper() != "N":
      validated += 1
    valString+= "validating if patient is infected:\n" + patient_data[3] + "\n"
    # print(life_timer_h)

    print(valString)
    if validated == 0:
      return True
    else:
      return False