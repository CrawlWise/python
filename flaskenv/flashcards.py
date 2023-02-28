from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my flash card program"


@app.route("/date")
def date():
    return "this page was served at" + str(datetime.now())


#shows how many times this page is viewed
counter = 0
@app.route("/views")
def count_views():
    global counter
    counter +=1
    return "this page is viewed " + str(counter) + " times"



#Before runing your application, use the line of code below
#$env:FLASK_APP=flashcode.py
#$env:FLASK_ENV=development

@app.route("/add_card", methods=["GET","POST"])
def add_cards():
    if request.method == "POST":
        return redirect("jw.org")
        #code goes in here
    else:
        return render_template("add_card.html")