import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///socialstories.db")

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Input your username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Input your password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Wrong password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Receive userinput about username and password, and see if it fits the conditions asked for
        db.execute("CREATE TABLE IF NOT EXISTS 'users' ('id' INTEGER NOT NULL, 'username' TEXT NOT NULL UNIQUE, 'hash' TEXT NOT NULL, PRIMARY KEY(id))")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
            return apology("You need to fill in each box")
        if password != confirmation:
            return apology("Passwords need to match")
        # Attempt to insert into username and password, which are unique columns. If this doesn't work, then return apology ("Username already exists")
        # TA told me about try and except; used Python documentation to figure out how to use this in program: https://www.w3schools.com/python/python_try_except.asp
        try:
            query = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, generate_password_hash(password))
        except:
            return apology("Username already taken")
        # Set session id to the result of the query, which is the id number
        session["user_id"] = query
        return redirect("/layout")
    else:
        return render_template("register.html")

@app.route("/layout", methods=["GET", "POST"])
def layout():
    if request.method == "GET":
        return render_template("layout.html")

def dq1():
    if request.method =="GET":
        return render_template("/socialdistancingstory/dq1.html")