import cherrypy
import os
import json
import cv2
import qrcode
import numpy as np

class AppServer(object):
    def CORS():
        if cherrypy.request.method == 'OPTIONS':
            cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
            cherrypy.response.headers['Access-Control-Allow-Headers'] = 'content-type'
            cherrypy.response.headers['Access-Control-Allow-Origin']  = '*'
            return True
        else:
            cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
    
    cherrypy.tools.CORS = cherrypy._cptools.HandlerTool(CORS)

    @cherrypy.expose
    def index(self):
        return "Genobank.io (TM) API"

    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def read_qrcode(self, file, data):
        # # Encriptar
        # sample = "https://genobank.io/certificates/verify-certificate-v1#Daniel%20Francisco%20Uribe%20Benitez%7CG29397810%20MALE%2045%7C2%7CN%7CFM-MDE-89722%7C1642255500000%7C5%7C0x87451c8d50b21f104a8e80f735c774ed223f706532c66b2a8c23980b595b9b412e379373d225d1c1341d96b6d89b3d34dc0483215652281bbd75b97e0fae5c491b%7C1642255576067%7C0x6225a9eacd9ccaec67eca298968f14d98093575f41bd856ffbddd90ded10b17817e122a4fe7a49161eacebf6e060d99182fe92d7d6e122d639f875a3b0c9c2831c%7C0x301068a4e5c335ece530dbb930d62c5d4c96b903fc01b1c03460d15c9f435113"
        # filename = "sitegenobank.png"
        # img = qrcode.make(sample)
        # img.save(filename)

        # # Decriptar
        # img = cv2.imread("sitewiki.png")
        # detector = cv2.QRCodeDetector()
        # data, bbox, straight_qrcode = detector.detectAndDecode(img)

        # print(data)

        print(file)
        print(data)

        file = file.file
        file = file.read()
        # decode binary to image
        img = cv2.imdecode(np.fromstring(file, np.uint8), cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()
        dato, bbox, straight_qrcode = detector.detectAndDecode(img)

        # # # print(file)
        # print("\nDato", dato, "\n")


        return dato

class GenoBank(object):
    def __init__(self):
        return None

    def start (self, port=5000):
        config = {
            'global': {
                'server.socket_host': '0.0.0.0',
                'server.socket_port': int(os.environ.get('PORT', port)),
            },
            '/': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd())
            }
        }
        cherrypy.quickstart(AppServer(), '/', config=config)