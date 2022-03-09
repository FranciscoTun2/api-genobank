import cherrypy
import os
import json

class AppServer(object):
    @cherrypy.expose
    def index(self):
        return "Genobank.io (TM) API"


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def read_qrcode(self):
        _json = cherrypy.request.body.read()
        _json = json.loads(_json)
        return _json

class GenoBank(object):

    def __init__(self):
        return None

    def start (self, port=5000):
        config = {
            'global': {
                'server.socket_host': '0.0.0.0',
                'server.socket_port': int(os.environ.get('PORT', port)),
            }
        }

        cherrypy.quickstart(AppServer(), '/', config=config)