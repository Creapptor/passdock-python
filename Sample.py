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

#   Sample.py: Passdock Python engine demo
#   Copyright (C) 2012 Creapptor SA <info@creapptor.com>
#   Contributors: Filippo Bigarella <filippo@filippobiga.com>


import passdock
import json
import time
 
# Grab your API token from https://api.passdock.com/settings
 
PASSDOCK_API_KEY="d3c2408d8d31523f08dc7851c5948b17"

if __name__ == "__main__":
    
    p = passdock.PassDock(PASSDOCK_API_KEY)
    
    # Fetch the json of a pass
    jsonResponse = p.fetchPass("2538", "1405") # pass_id and then template_id
    
    # Create a pass
    """
        newPassDict = {
        
        'serial_number' :  "PYAPI-%f" % time.time(),
        'gate': { 'value' : 'PYGATE' },
        'bar' : { 'message' : 'PY: This is the message inside the QR Code.' }
        
        }
        
        jsonResponse = p.createPass(newPassDict, "23")
    """
    
    # Update pass
    """
        updateDict = { 'gate' : { 'value' : 'python_updated_value' } }
        jsonResponse = p.updatePass("80", "23", updateDict)
    """
    
    # Destroy a pass
    """
        jsonResponse = p.destroyPass("67", "23")
    """
    
    print json.dumps(jsonResponse, sort_keys=True, indent=4)
