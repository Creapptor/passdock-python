#!/usr/bin/env python

#
#	Copyright (C) 2012 Creapptor SA <info@creapptor.com>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#   PassDock.py: PassDock API
#   Copyright (C) 2012 Creapptor SA <info@creapptor.com>
#   Contributors: Filippo Bigarella <filippo@filippobiga.com>


'''
    
    This module includes the 'Passdock' class (restkit.Resource subclass)
    which allows you to talk to the PassDock RESTful APIs
    
    Example usage:
    p = PassDock(baseURL, apiKey)
    jsonResponse = p.fetchPass(passID, templateID)
    print json.dumps(jsonResponse, indent=4)
    
    More examples can be found inside Sample.py
    
'''

from restkit import Resource
import json

BASE_URL = "http://api.passdock.com/api"


class PassDock(Resource):
    
    def __init__(self, api_key, pool_instance=None, **kwargs):
        
        self.apiKey = api_key
        super(PassDock, self).__init__(BASE_URL, follow_redirect=True,
                                       max_follow_redirect=10,
                                       **kwargs)
    
    
    
    
    def fetchPass(self, passID, templateID):
        apiPath = "/v1/templates/" + templateID + "/passes/" + passID
        return self.get(apiPath, api_token=self.apiKey)
    
    
    
    def downloadPass(self, passID, templateID):
        apiPath = "/v1/templates/" + templateID + "/passes/" + passID
        return self.get(apiPath, api_token=self.apiKey, show=true)
    
    
    
    def createPass(self, passDict, templateID):
        encoder = json.JSONEncoder()
        passJSON = encoder.encode(passDict)
        
        requestParamsDict = {
            'debug':'true',
            'errors':'true',
            'pass' : passJSON,
            'api_token' : self.apiKey
        }
        
        apiPath = "/v1/templates/" + templateID + "/passes"
        return self.post(path=apiPath, params_dict=requestParamsDict)
    
    
    
    
    def updatePass(self, passID, templateID, passDict):
        encoder = json.JSONEncoder()
        passJSON = encoder.encode(passDict)
        requestParamsDict = {
            'debug':'true',
            'errors':'true',
            'pass' : passJSON,
            'api_token' : self.apiKey
        }
        
        apiPath = "/v1/templates/" + templateID + "/passes/" + passID
        return self.put(path=apiPath, params_dict=requestParamsDict)
    
    
    
    
    def destroyPass(self, passID, templateID):
        apiPath = "/v1/templates/" + templateID + "/passes/" + passID
        
        requestParamsDict = {
            'debug':'true',
            'errors':'true',
            'api_token' : self.apiKey
        }
        
        return self.delete(path=apiPath, params_dict=requestParamsDict)
    
    
    
    
    def request(self, *args, **kwargs):
        resp = super(PassDock, self).request(*args, **kwargs)
        
        try:
            bodyString = resp.body_string()
            return json.loads(bodyString)
        except:
            return None
