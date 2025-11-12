from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/validate",  methods=["POST"])
def validate():
    uname = request.form.get('username')
    passwd = request.form.get('password')
    role = request.form.get('role')
    """
    if uname == 'praveen' and passwd == '12345':
        #return "<h2> Valid User</h2>"
        return render_template("success.html", user=uname)
    else:
       #return "<h2>Invalid User</h2>"
       return render_template("fail.html", user=uname)
    """
    return render_template("success.html", user=uname)
    
if __name__ == '__main__':
    app.run(debug=True,port=8082)