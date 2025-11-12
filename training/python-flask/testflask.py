from  flask import Flask, request

app = Flask(__name__)


@app.route("/info", methods=["POST"])
def info():
    data = request.get_json()
    empno = data.get('id')
    ename = data.get('name')
    desc = data.get("description")
    return f" Hello {ename} your id is {empno} and you have {desc} Personality"


"""
int - integer
float - floating point numbers (deciman numbers)
path - text with slashes
uuid - 

"""
@app.route("/add/<int:a>/<int:b>")
def addition(a,b):
    sum = a+b
    return f"The sum is {sum}"


@app.route("/greet/<name>/<country>")
def greet(name,country):
    return f"Hello {name} welcome to {country}"


@app.route("/")
def home():
    return "Welcome to Flask "

@app.route("/test", methods=["POST"])
def test():
    return "Test end point is for post is called..!", 200

@app.route("/put", methods=["PUT"])
def test1():
    return "Test end point for put is  called..!", 200


@app.route("/del", methods=["DELETE"])
def test2():
    return "Test end point for delete is called..!", 200



if __name__ == "__main__":
    app.run(debug=True, port=8081)