import json
class patient:
  def data_to_class(self, data):
    try:
      data = json.loads(data)
    except:
      raise Exception("Invalid json")
    return data