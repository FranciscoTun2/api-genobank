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
        file = file.file
        file = file.read()
        # decode binary to image
        img = cv2.imdecode(np.fromstring(file, np.uint8), cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()
        dato, bbox, straight_qrcode = detector.detectAndDecode(img)
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