import os
from os import path
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, request, reqparse
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
api = Api(app)
ALLOWED_EXTENTIONS = ['jpg', 'jpeg', 'png']

location = 'data'


class UploadImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('video', type=str)
        parser.add_argument('fname', type=str)
        args = parser.parse_args()
        file = request.files['video']
        name = args['fname']

        if not path.exists(location):
            os.makedirs(location + '/data')

            secname = path.join(location + '/data', name)
            print(secname)
            file.save(secure_filename(secname))
        return '{"status":200, "message": "File Uploaded successfully"}'


api.add_resource(UploadImage, '/upload')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
