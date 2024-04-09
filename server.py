from flask import Flask
from flask_restful import Resource, Api
import logging 

app = Flask("VideoAPI")
api = Api(app)

logging.basicConfig(level=logging.DEBUG)

class Video(Resource):
    
    def get(self):
        app.logger.info("Received GET request for /")
        return "Hello World"

api.add_resource(Video, '/')

if __name__ == '__main__':
    app.run(debug=false,host='0.0.0.0')
