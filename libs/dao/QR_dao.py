from datetime import datetime

class QR:
  def __init__(self):
    self.table = "QRTable"
    self.taxonomy = None
    self.added = 0

  def validate_data(self, data):
    splitUrl = data.split("#")
    if len(splitUrl) == 2:
      data = splitUrl[1].replace("%20", " ").split("%7C")
      data_time = data[8]

      # parse datetime.now to timestamp
      now = datetime.now()
      now_timestamp = now.timestamp()

      now_timestamp = int(now_timestamp * 1000)

      # now = int(now)



      print(data_time)
      print(now_timestamp)
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