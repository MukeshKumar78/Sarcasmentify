from flask import request
from flask_restful import Api, Resource, reqparse
from models import LSTMClassifier

lstm = LSTMClassifier()
print(lstm.predict('hello'))
class PredictionHandler(Resource):
    def post(self):
        print(request.json)
        return {}
        

