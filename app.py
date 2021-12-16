import os
from flask import Flask, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("home.html")


# If running from this file, run flask app.
if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )