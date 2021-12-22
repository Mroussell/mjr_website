import os
from flask import Flask, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("home.html")

@app.route("/portfolio", methods=['GET', 'POST']) 
def portfolio():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home.html'))
    return render_template("portfolio.html")


@app.route("/contact") 
def contact():
    return render_template("contact.html")


@app.route("/blog") 
def blog():
    return render_template("blog.html")


# If running from this file, run flask app.
if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )