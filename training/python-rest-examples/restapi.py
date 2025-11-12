from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
       return {"message":" Hello World"}
    
    def post(self):
       return {"message":"Post Method is called..!"}
    
    def put(self):
       return {"message":"Put Method is called..!"}

# Api end points
api.add_resource(Hello, "/")

if __name__ == '__main__':
 app.run(debug=True)