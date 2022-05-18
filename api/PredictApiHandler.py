from flask_restful import Api, Resource, reqparse, request
import json

from models import LSTMClassifier

lstm = LSTMClassifier()
class PredictApiHandler(Resource):
    def get(self):
        return {}

    def post(self): 
        text = request.json['text']
        prediction = lstm.predict(text)
        return {'prediction': prediction[0]}
