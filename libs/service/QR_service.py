from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.dao import QR_dao
import numpy as np
import cv2

from pyzbar import pyzbar 
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes


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

  def decode_qr_pdf(self, file):
    try:
      qr_code = pyzbar.decode(file)[0]
      data = qr_code.data.decode("utf-8").encode("shift-jis").decode("utf-8")
      return data
    except:
      return False

  def jsonify(self, dato):
    try:
      dato = dato.split("#")[1]
      dato = dato.replace("%20", " ")
      arrayData = dato.split("%7C")
      jsonData = {}
      jsonData["arrayData"] = arrayData
      jsonData["validated"] = True 
      return jsonData
    except:
      return {"validated": False}
      # raise Exception("Error durin Jsonify. Wrong QR code data")
    