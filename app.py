import os
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS #comment this on deployment
from api.PredictApiHandler import PredictApiHandler
import gdown

models = {
    'bert': 'https://drive.google.com/uc?id=1-1wuhs5UrTPrIMGuO8wdisfopZgxTqIE',
    'lstm': 'https://drive.google.com/uc?id=1-6ZAr2gZ4XIMqNRTSQ0ZweM6C762UbOv',
    'bayes': 'https://drive.google.com/uc?id=1-6ZAr2gZ4XIMqNRTSQ0ZweM6C762UbOv',
}

for model, url in models.items():
    if not os.path.exists(f'models/{model}.pkl'):
        gdown.download(url, f'models/{model}.pkl')

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

api.add_resource(PredictApiHandler, '/api/predict')

