from flask import Flask, jsonify, request
from ner import SpacyDocument
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



class Basic(Resource):

    def get(self):
        return jsonify('You can get the tokens of your string from this extremely minimal website.')

    # curl http://127.0.0.1:5000/ -H "Content-Type: text/plain" -d 'insert sentence here'
    def post(self):
        some_string = str(request.data)
        process_result = SpacyDocument(some_string)
        return jsonify({'result': (process_result.get_tokens())})


api.add_resource(Basic, '/')

if __name__ == '__main__':
    app.run(debug=True)
