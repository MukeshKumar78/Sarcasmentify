import os
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS #comment this on deployment
from api.NewsApiHandler import NewsApiHandler

env = os.getenv('FLASK_ENV')
app = Flask(__name__, 
            static_url_path = '', 
            static_folder = 'client/public' if env == 'dev' else 'client/build')
CORS(app)
api = Api(app)
app.secret_key = "waowaowaowaowaowaowao"


@app.route('/', defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder or '', 'index.html')

api.add_resource(NewsApiHandler, '/api/news')

