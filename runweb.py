import cherrypy
import os
import json

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Genobank.io (TM) API"


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def read_qrcode(self):
        _json = cherrypy.request.body.read()
        _json = json.loads(_json)
        return _json

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
}

cherrypy.quickstart(HelloWorld(), '/', config=config)