# Passdock Python API tool

Passdock let you design, create, manage, update and deploy Passbook passes.

Use its APIs to integrate Passdock in your environment.

### Requirements

You can install RestKit using the following commands:

	curl -O http://python-distribute.org/distribute_setup.py
	sudo python distribute_setup.py
	sudo easy_install pip
	sudo pip install http-parser
	sudo pip install restkit

### Quick Start

Get your API key from [Passdock](https://api.passdock.com/settings) and set it.

    PASSDOCK_API_KEY="YOUR_API_KEY_HERE"

Import dependancies

    import passdock
    import json
    import time

In the main function write 

    if __name__ == "__main__":
    
        p = passdock.PassDock(PASSDOCK_API_KEY)
        
        # Fetch the json of a pass
        jsonResponse = p.fetchPass("PASS_ID", "TEMPLATE_ID")

        print json.dumps(jsonResponse, sort_keys=True, indent=4)
        
See Sample.py for usage examples.