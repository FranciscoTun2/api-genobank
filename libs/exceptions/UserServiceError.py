import cherrypy

class UserServiceError(Exception):
    def __init__(self,msg):
        super(UserServiceError, self).__init__(msg)

#Avocado Blockchain Services at Merida Yucatan
