from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route("/sign_up", methods = ["GET"])
def sign_up():
    return render_template("sign_up.html")

if __name__== "__main__":
    app.run()