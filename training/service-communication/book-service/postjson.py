from flask import Flask, jsonify
from flask_restful import Api, Resource
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

app = Flask(__name__)
api = Api(app)

class FetchData(Resource):
    def get(self,postid):
        url = f"{BASE_URL}/{postid}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json(), 200
        else:
            return {"message":" Post Data not found "}, 404
        
api.add_resource(FetchData, "/<int:postid>")

if __name__ == "__main__":
    app.run(debug=True, port= 5002)