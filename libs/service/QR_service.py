from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.dao import QR_dao
import numpy as np
import cv2
from pyzbar import pyzbar 
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
# import pytesseract

class QR_service:
  def __init__(self, _qr):
    if not isinstance(_qr, QR_dao.QR):
      raise DomainInjectionError.DomainInjectionError("QR_service", "Qr")
    self.qr = _qr
    self.encryption = Encryption.Encryption()

  def decode(self, file):
    file = file.file
    file = file.read()
    img = cv2.imdecode(np.fromstring(file, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    dato, bbox, straight_qrcode = detector.detectAndDecode(img)
    print("\n\n",dato,"\n\n")
    return dato

  def decodePyzbar(self, file):
    image = Image.open(file.file)
    qr_code = pyzbar.decode(image)[0]
    print(qr_code)
    data = qr_code.data.decode("utf-8").encode("shift-jis").decode("utf-8")
    return data

  def pdf_to_image(self, file):
    images = convert_from_bytes(file.file.read())
    return images

  # def get_text_from_pdf (self, image):
  #   try:
  #     image = image.fp
  #     print(image)
  #     # b64File = image.convert('RGB').tobytes()
  #     text = pytesseract.image_to_string(image)
  #     # print(text)

  #   except:
  #     raise

  def decode_qr_pdf(self, file):
    try:
      qr_code = pyzbar.decode(file)[0]
      data = qr_code.data.decode("utf-8").encode("shift-jis").decode("utf-8")
      return data
    except:
      return False

  def validate_data(self, json_data, name):
    if "arrayData" in json_data:
      patiend_data = json_data["arrayData"]
      if len(patiend_data) == 11:
        if len(name) > 0:
          validated = self.qr.validate_data(patiend_data, name)
          if not validated:
            return {"validated": False}
          else:
            json_data["validated"] = validated
    
    return json_data


  def jsonify(self, dato):
    try:
      dato = dato.split("#")[1]
      dato = dato.replace("%20", " ")
      arrayData = dato.split("%7C")
      jsonData = {}
      jsonData["arrayData"] = arrayData
      # jsonData["validated"] = True 
      return jsonData
    except:
      return {"validated": False}
      # raise Exception("Error durin Jsonify. Wrong QR code data")
    