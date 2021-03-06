import cherrypy
import os
import json
from libs import database
from libs.dao import QR_dao
from libs.dao import patient_dao
from libs.dao import genotype_dao
from libs.dao import ipfs_dao
from libs.service import QR_service
from libs.service import patient_service
from libs.service import genotype_service
from libs.service import ipfs_service
class AppServer(object):
    def __init__(self):
        self.db = database.database()
        qr_dao = QR_dao.QR()
        pattient_dao = patient_dao.patient_dao(self.db.con)
        geno_dao = genotype_dao.genotype_dao(self.db.con)
        ipfs_daoi = ipfs_dao.ipfs()
        self.qr_service = QR_service.QR_service(qr_dao)
        self.patient_service = patient_service.patient_service(pattient_dao)
        self.geno_service = genotype_service.genotype_service(geno_dao)
        self.ipfs_servicei = ipfs_service.ipfs_service(ipfs_daoi)

    def CORS():
        if cherrypy.request.method == 'OPTIONS':
            cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
            cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
        
            # cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
            # cherrypy.response.headers['Access-Control-Allow-Headers'] = 'content-type'
            # cherrypy.response.headers['Access-Control-Allow-Origin']  = '*'
            return True
        else:
            cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
    cherrypy.tools.CORS = cherrypy._cptools.HandlerTool(CORS)

    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
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
    def validate_pdf(self, file, name):
        try:
            pdf_image = self.qr_service.pdf_to_image(file)
            data = self.qr_service.decode_qr_pdf(pdf_image[0])
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
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def generate_token_id(self, token):
        id_token = self.geno_service.generate_token_id(token)
        print(id_token)
        return str(id_token)
    
    # TODO: recives a JSON in the body with the signature
    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def consents(self, data, file):
        try:
            data = json.loads(data)
            nft_hash = self.geno_service.create_nft(data)
            data["nft_hash"] = nft_hash
            if not nft_hash:
                raise Exception("Error during genotype creation")
            self.geno_service.create(data, file)
            return {"transaction_hash": nft_hash}
        except:
            raise

    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def save_file(self, data, file):
        try:
            data = json.loads(data)
            file_name = self.geno_service.save_file_test(data, file)
            return {"file_name" : file_name}
        except:
            raise
    

    # testing
    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.tools.json_out()
    def test(self):
        address = "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db"
        # parse address to int 
        id_address = int(address, 16)
        print(address)
        print(id_address)
        _json = {
            "address": address,
            "id": id_address,
        }
        return _json
        
    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.tools.json_out()
    def all_patients(self):
        patient = self.patient_service.all_patients()
        return self.patient_service.jsonify(patient)
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