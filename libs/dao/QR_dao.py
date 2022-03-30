from datetime import datetime
from numpy import double

class QR:
  def __init__(self):
    self.table = "QRTable"
    self.taxonomy = None
    self.added = 0

  def validate_data(self, patient_data, name):
    validated = 0
    print("\n\npatiend data:",patient_data[11],"\n\n")
    life_time = (float(datetime.now().timestamp())) - (float(int(patient_data[11])/1000))
    life_timer_h = life_time / (3600)

    # resume
    print("Patient Name", patient_data[0].upper())
    print("Patient Procedure", patient_data[2])
    print("life_timer_h", life_timer_h)
    print("Patient Result", patient_data[3])



    if patient_data[0].upper() != name.upper():
      validated += 1

    if int(patient_data[2]) == 1:
      if life_timer_h > 48:
        validated += 1

    if int(patient_data[2]) == 2:
      if life_timer_h > 24:
        validated += 1

    if patient_data[3].upper() != "N":
      validated += 1
    # print(life_timer_h)

    if validated == 0:
      return True
    else:
      return False