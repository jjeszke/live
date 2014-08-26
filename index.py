# coding=utf-8
__author__ = 'Jakub.Jeszke'

import cherrypy

class live(object):

    @cherrypy.expose
    def index(self):
        return "test"

cherrypy.config.update("server.conf")
cherrypy.quickstart(live())