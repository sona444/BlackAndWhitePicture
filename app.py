from flask import Flask, make_response, render_template, request
from dotenv import load_dotenv
from flask_restful import Resource, Api
from PIL import Image
import os

load_dotenv()

app = Flask(__name__)
api=Api(app)

class main(Resource):
    def get(self):
        return make_response(render_template('index.html'))

class upload_dataset(Resource):
    def post(self):
        f = request.files['file']
        for file in os.listdir('static/img'):
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                os.remove('static/img/'+file) 
        filename=f.filename
        path='{}/{}'.format('static/img',filename)
        f.save(path)
        img = Image.open(path)
        imgGray = img.convert('L')
        imgGray.save('static/img/'+filename)
        return make_response(render_template('index.html',image=filename))
        
class all_pictures(Resource):
    def get(self):
        return make_response(render_template('index.html'))

api.add_resource(main,'/')
api.add_resource(upload_dataset,'/upload')

if __name__ == '__main__':
    app.run(debug=True)