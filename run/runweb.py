import cherrypy
import os
from libs import database
from libs.dao import QR_dao
from libs.dao import patient_dao
from libs.service import QR_service
from libs.service import patient_service


class AppServer(object):
    def __init__(self):
        self.db = database.database()
        qr_dao = QR_dao.QR()
        pattient_dao = patient_dao.patient_dao(self.db.con)
        self.qr_service = QR_service.QR_service(qr_dao)
        self.patient_service = patient_service.patient_service(pattient_dao)

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
        dato = self.qr_service.decode(file)
        _json= self.qr_service.jsonify(dato)
        return dato,_json

    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def sign_up(self, data):
        data = self.patient_service.patient.validate(data)
        self.patient_service.create(data)
        # print("\n\n",data,"\n\n")
        # self.patient_service.create(data)

        
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