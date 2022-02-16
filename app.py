"""
MJR
Michael Roussell
Copyright 2022

Please run from this file.

Python 3.9.7 version of the python interpreter.
If there are any questions, please contact me at 'mjr.dev.contact@gmail.com.

MIT Education License Preferred.
"""
import os
from dotenv import load_dotenv
from contact import ContactHandler
from dbhandler import DBHandler
from flask import Flask, flash, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("FLASK_SEC_KEY")

@app.route("/", strict_slashes=False)
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


@app.route("/contact", methods=['GET', 'POST']) 
def contact():
    cth = ContactHandler()
    if request.method == 'POST':
        print("Initialize Email")
        name = request.form["full-name"]
        subject = request.form["subject"]
        subject = name + " | " + subject
        body = request.form["message"] + "\n ~ " + request.form["email-address"]
        print(f"Email Subject: {subject}")
        print(f"Email Body: {body}")
        cth.sendContactEmail(subject, body)
        flash("We got your message and will be in touch soon. Thank you!")
        return render_template("contact.html",  scrollToAnchor="flashes")
    return render_template("contact.html")


@app.route("/blog") 
def blog():
    return render_template("blog.html")


@app.route("/portfolio/tech") 
def tech():
    dbh = DBHandler()
    db_results = dbh.inspect_table('tech_projects_test_3')
    post_list = []
    for post in db_results:
        post['body'] =  post['body'].replace('\\n', '\n\n').replace('\\t', '\t')
    return render_template("tech-page.html", db_results=reversed(db_results))

@app.route("/portfolio/data") 
def data():
    return render_template("data-page.html")


# If running from this file, run flask app.
if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )