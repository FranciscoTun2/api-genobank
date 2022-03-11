from libs.domain import Encryption
from libs.exceptions import DomainInjectionError
from libs.domain import QR
import numpy as np
import cv2
class QR_service:
  def __init__(self, _qr):
    if not isinstance(_qr, QR.QR):
      raise DomainInjectionError.DomainInjectionError("QR_service", "Qr")
    self.qr = _qr
    self.encryption = Encryption.Encryption()

  def decode(self, file):
    file = file.file
    file = file.read()
    img = cv2.imdecode(np.fromstring(file, np.uint8), cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    dato, bbox, straight_qrcode = detector.detectAndDecode(img)
    print(dato)
    return dato

  def jsonify(self, dato):
    try:
      dato = dato.split("#")[1]
      dato = dato.replace("%20", " ")
      arrayData = dato.split("%7C")
      jsonData = {}
      jsonData["arrayData"] = arrayData
      return jsonData
    except:
      raise Exception("Error durin Jsonify. Wrong QR code data")
    