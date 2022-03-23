import cherrypy
import os
from libs import database
from libs.dao import QR_dao
from libs.dao import patient_dao
from libs.dao import ipfs_dao
from libs.service import QR_service
from libs.service import patient_service
from libs.service import ipfs_service
class AppServer(object):
    def __init__(self):
        self.db = database.database()
        qr_dao = QR_dao.QR()
        pattient_dao = patient_dao.patient_dao(self.db.con)
        ipfs_daoi = ipfs_dao.ipfs()
        self.qr_service = QR_service.QR_service(qr_dao)
        self.patient_service = patient_service.patient_service(pattient_dao)
        self.ipfs_servicei = ipfs_service.ipfs_service(ipfs_daoi)

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
    def pin_ipfs(self, img_data):
        ipfs_upload = self.ipfs_servicei.pin_ipfs(img_data)
        return ipfs_upload

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
    def validate_pdf(self, file, name):
        try:
            pdf_image = self.qr_service.pdf_to_image(file)
            # text = self.qr_service.get_text_from_pdf(pdf_image[0])
            data = self.qr_service.decode_qr_pdf(pdf_image[0])
            # validated = self.qr_service.validate_data(data)
            # if not data:
            #     return {"validated": False}
            _json = self.qr_service.jsonify(data)
            _json = self.qr_service.validate_data(_json, name)
            if _json["validated"]:
                return data, _json
            else:
                return _json
        except:
            raise 
    
    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def sign_up(self, data):
        data = self.patient_service.patient.validate(data)
        self.patient_service.create(data)

    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.tools.json_out()
    def all_patients(self):
        return self.patient_service.all_patients()

class GenoBank(object):
    def __init__(self):
        return None

    def start (self, port=8080):
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