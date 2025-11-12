from flask import Flask, redirect, url_for, render_template, request, abort


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login1.html")


@app.route("/success")
def success():
    return "logged in successfully...!"



@app.route("/login", methods=["GET","POST"])
def login():
    uname = request.form["username"]
    if request.method == "POST" and uname =="admin":
      
        return redirect(url_for("success"))
    else:
        if uname[0].isdigit():
            abort(400)
        


if __name__ == '__main__':
    app.run(debug=True, port=5001)