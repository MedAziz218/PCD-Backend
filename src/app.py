import os
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    
    # this is just to prevent flask from starting twice in debug mode 
    # TODO: remove this when development is done
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        from routes import routes_init
        from db import mongo_connection
        
        api = routes_init(app)
        assert mongo_connection is not None
    
    app.run(host="0.0.0.0", debug=True )
