import cherrypy
import os
import json
import cherrypy_cors

class AppServer(object):
    def CORS():
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'

        # if cherrypy.request.method == 'OPTIONS':
        #     cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        #     cherrypy.response.headers['Access-Control-Allow-Headers'] = 'content-type'
        #     cherrypy.response.headers['Access-Control-Allow-Origin']  = '*'
        #     return True
        # else:
        #     cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
    
    cherrypy.tools.CORS = cherrypy._cptools.HandlerTool(CORS)

    @cherrypy.expose
    def index(self):
        return "Genobank.io (TM) API"

    @cherrypy.expose
    @cherrypy.config(**{'tools.CORS.on': True})
    @cherrypy.tools.allow(methods=['POST'])
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
            },
            '/static': {
                'tools.staticdir.on': True,
                'cors.expose.on': True,
            }
        }

        cherrypy.quickstart(AppServer(), '/', config=config)