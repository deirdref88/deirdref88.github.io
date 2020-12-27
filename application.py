import os
import smtplib
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
# Used helpers.py from Finance pset
from helpers import apology, login_required
import urllib.parse as up
import psycopg2
up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["DATABASE_URL"])
# conn = psycopg2.connect(
#  database=url.path[1:],
#  user=url.username,
#  password=url.password,
#  host=url.hostname,
#  port=url.port
# )

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
# db = SQL(os.environ["DATABASE_URL"])

# Render the homepage
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    pass 
    # Forget any user_id
    # session.clear()

    # # User reached route via POST (as by submitting a form via POST)
    # if request.method == "POST":

    #     # Ensure username was submitted
    #     if not request.form.get("username"):
    #         return apology("Input your username")

    #     # Ensure password was submitted
    #     elif not request.form.get("password"):
    #         return apology("Input your password")

    #     # Query database for username
    #     rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

    #     # Ensure username exists and password is correct
    #     if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
    #         return apology("Wrong password")
    #     session["user_id"] = rows[0]["id"]
    #     # find out which preferences the user has
    #     avatar = db.execute("SELECT avatar FROM users WHERE username = ?", request.form.get("username"))
    #     sound = db.execute("SELECT sound FROM users WHERE username = ?", request.form.get("username"))
    #     color = db.execute("SELECT color FROM users WHERE username = ?", request.form.get("username"))
    #     # Remember which user has logged in and remember their preferences as session[]
    #     session["username"] = request.form.get("username")
    #     session["link"] = avatar[0]['avatar']
    #     session["sound"] = sound[0]['sound']
    #     session["color"] = color[0]['color']
    #     session["user_id"] = rows[0]["id"]

    #     # Redirect user to home page
    #     return redirect("/")

    # # User reached route via GET (as by clicking a link or via redirect)
    # else:
    #     return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/forgotpassword", methods=["GET", "POST"])
def forgotpassword():
    """Retrieves reset password page if user has forgotten password"""
    pass
    # if request.method == "GET":
    #     return render_template("forgotpassword.html")
    # if request.method == "POST":
    #     # Retreive username from form
    #     username = request.form.get("username")
    #     # Retrieve security question for associated username
    #     security = db.execute("SELECT securityq FROM users WHERE username = ?", username)
    #     try:
    #         securityq = security[0]['securityq']
    #     except:
    #         # Return apology if an invalid username is inputted
    #         return apology("Invalid Username")
    #     # Send user to reset password page, along with their securityq information
    #     return render_template("resetpassword.html", securityq=securityq, username=username)

@app.route("/resetpassword", methods=["GET", "POST"])
def resetpassword():
    pass
    # """Allow users to reset password if they forgot it"""
    # if request.method =="GET":
    #     return render_template("resetpassword.html")
    # if request.method == "POST":
    #     # Get user answers from form: their username, their securityq (automatically filled out from forgotpassword), their answer, new password, and confirm new password
    #     username = request.form.get("username")
    #     securityq = request.form.get("securityq")
    #     response = request.form.get("response")
    #     password = request.form.get("password")
    #     confirmation = request.form.get("confirmation")

    #     try:
    #         # Check to see if username is correct and retrieve corresponding answer to that users security question
    #         answer = db.execute("SELECT securitya FROM users WHERE username = ?", username)
    #     except:
    #         return apology("Invalid Username")

    #     answers = answer[0]["securitya"]
    #     # Check to see if answers in sql database matches user response
    #     if answers != response:
    #         return apology("Incorrect answer to security question")
    #     if answers == response:
    #         # If they do match, update users password and redirect back to login
    #         db.execute("UPDATE users SET hash = ? WHERE username = ?", generate_password_hash(password), username)
    #         return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    pass 
    # """Register user"""
    # if request.method == "POST":
    #     # Receive user input about username, password, and their personal preferences
    #     username = request.form.get("username")
    #     password = request.form.get("password")
    #     confirmation = request.form.get("confirmation")
    #     avatar = request.form.get("pickavatar")
    #     securityq = request.form.get("securityq")
    #     securitya = request.form.get("security")
    #     color = request.form.get("pickcolor")
    #     sound = request.form.get("sound")
    #     if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation") or not request.form.get("pickavatar") or not request.form.get("security") or not request.form.get("sound") or not request.form.get("pickcolor"):
    #         return apology("You have missing information")
    #     if password != confirmation:
    #         return apology("Passwords need to match")

    #     # Attempt to insert into sql with username as a unique key; if it fails, username is already in use
    #     try:
    #         query = db.execute("INSERT INTO users (username, hash, avatar, securityq, securitya, color, sound) VALUES (?,?,?,?,?,?,?)", username, generate_password_hash(password), avatar, securityq, securitya, color, sound)
    #     except:
    #         return apology("Username already taken")
    #     # Set session id to the result of the query, which is the id number
    #     session["user_id"] = query
    #     return redirect("/login")
    # else:
    #     return render_template("register.html")

@app.route("/update", methods=["GET", "POST"])
def update():
    pass
    # """Update user preferences"""
    # if request.method == "POST":
    #     # Check each field to see if the user has filled it out to submit an update
    #     # If they have, update sql database
    #     if request.form.get("username"):
    #         try:
    #             db.execute("UPDATE users SET username = ? WHERE id = ?", request.form.get("username"), session["user_id"])
    #         except:
    #             return apology ("That username is already in use!")
    #     if request.form.get("password"):
    #         if not request.form.get("confirmation") or request.form.get("confirmation") != request.form.get("password"):
    #             return apology("Password needs to match confirm password")
    #         else:
    #             db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(request.form.get("password")), session["user_id"])
    #     if request.form.get("pickavatar"):
    #         db.execute("UPDATE users SET avatar = ? WHERE id = ?", request.form.get("pickavatar"), session["user_id"])
    #     if request.form.get("sound"):
    #         db.execute("UPDATE users SET sound = ? WHERE id = ?", request.form.get("sound"), session["user_id"])
    #     if request.form.get("pickcolor"):
    #         db.execute("UPDATE users SET color = ? WHERE id = ?", request.form.get("pickcolor"), session["user_id"])

    #     # Check to see if users have not chosen the default option (don't change, 'nope'). If they haven't, check to see if they have included an answer for new security question
    #     if request.form.get("securityq") != "nope":
    #         if not request.form.get("security"):
    #             return apology("You need to include an answer to your security question")
    #         else:
    #             db.execute("UPDATE users SET securityq = ?, securitya = ? WHERE id = ?", request.form.get("securityq"), request.form.get("security"), session["user_id"])
    #     # Check to see if users have included an answer but have not selected a security question
    #     if request.form.get("security"):
    #         if not request.form.get("securityq"):
    #             return apology("You need to include a security question for your answer")
    #     return redirect("/login")
    # else:
    #     return render_template("update.html")

@app.route("/contactus", methods=["GET", "POST"])
def contactus():
    pass
    # if request.method == "POST":
    #     name = request.form.get("name")
    #     email = request.form.get("email")
    #     message = request.form.get("message")
    #     if not request.form.get("message"):
    #         return apology("Please give us your message!")
    #     if not request.form.get("name") or not request.form.get("email"):
    #         return apology("Please include your contact information!")
    #     # Contact message sent to our email
    #     contact = "%s sent you a message: %s. This is their email address: %s" % (name, message, email)
    #     # https://www.youtube.com/watch?v=U5MBYN6an70
    #     # Source used to figure out how to send ourselves an email
    #     server = smtplib.SMTP("smtp.gmail.com", 587)
    #     server.starttls()
    #     # Server sends an email to deirdre with the contact message from catherine's email account
    #     server.login("catherine.sheepy.yang@gmail.com", "check50lol")
    #     server.sendmail("catherine.sheepy.yang@gmail.com", "deirdre.flanagan@yale.edu", contact)
    #     return redirect("/")
    # else:
    #     return render_template("contactus.html")
@app.route("/aboutus")
def aboutus():
    """About us page"""
    if request.method == "GET":
        return render_template("aboutus.html")

# The rest of the code is the app route to the ~46 pages of our social stories
@app.route("/dq1")
def dq1():
    if request.method =="GET":
        return render_template("dq1.html")

@app.route("/dq2")
def dq2():
    if request.method =="GET":
        return render_template("dq2.html")

@app.route("/dq3")
def dq3():
    if request.method =="GET":
        return render_template("dq3.html")

@app.route("/dq4")
def dq4():
    if request.method =="GET":
        return render_template("dq4.html")

@app.route("/dq5")
def dq5():
    if request.method =="GET":
        return render_template("dq5.html")

@app.route("/distance1")
def distance1():
    if request.method == "GET":
        return render_template("distance1.html")

@app.route("/distance2")
def distance2():
    if request.method == "GET":
        return render_template("distance2.html")

@app.route("/distance3")
def distance3():
    if request.method == "GET":
        return render_template("distance3.html")

@app.route("/distance4")
def distance4():
    if request.method == "GET":
        return render_template("distance4.html")
@app.route("/distance5")
def distance5():
    if request.method == "GET":
        return render_template("distance5.html")

@app.route("/distance6")
def distance6():
    if request.method == "GET":
        return render_template("distance6.html")

@app.route("/distance7")
def distance7():
    if request.method == "GET":
        return render_template("distance7.html")

@app.route("/distance8")
def distance8():
    if request.method == "GET":
        return render_template("distance8.html")

@app.route("/distance9")
def distance9():
    if request.method == "GET":
        return render_template("distance9.html")

@app.route("/distance10")
def distance10():
    if request.method == "GET":
        return render_template("distance10.html")

@app.route("/distance11")
def distance11():
    if request.method == "GET":
        return render_template("distance11.html")

@app.route("/distance12")
def distance12():
    if request.method == "GET":
        return render_template("distance12.html")

@app.route("/distance13")
def distance13():
    if request.method == "GET":
        return render_template("distance13.html")

@app.route("/masks1")
def masks1():
    if request.method =="GET":
        return render_template("masks1.html")

@app.route("/masks2")
def masks2():
    if request.method =="GET":
        return render_template("masks2.html")

@app.route("/masks3")
def masks3():
    if request.method =="GET":
        return render_template("masks3.html")

@app.route("/masks4")
def masks4():
    if request.method =="GET":
        return render_template("masks4.html")

@app.route("/masks5")
def masks5():
    if request.method =="GET":
        return render_template("masks5.html")

@app.route("/masks6")
def masks6():
    if request.method =="GET":
        return render_template("masks6.html")

@app.route("/masks7")
def masks7():
    if request.method =="GET":
        return render_template("masks7.html")

@app.route("/masks8")
def masks8():
    if request.method =="GET":
        return render_template("masks8.html")

@app.route("/masks9")
def masks9():
    if request.method =="GET":
        return render_template("masks9.html")

@app.route("/masks10")
def masks10():
    if request.method =="GET":
        return render_template("masks10.html")

@app.route("/masks11")
def masks11():
    if request.method =="GET":
        return render_template("masks11.html")

@app.route("/masks12")
def masks12():
    if request.method =="GET":
        return render_template("masks12.html")

@app.route("/masks13")
def masks13():
    if request.method =="GET":
        return render_template("masks13.html")

@app.route("/masks14")
def masks14():
    if request.method =="GET":
        return render_template("masks14.html")

@app.route("/masks15")
def masks15():
    if request.method =="GET":
        return render_template("masks15.html")

@app.route("/mq1")
def mq1():
    if request.method == "GET":
        return render_template("mq1.html")

@app.route("/mq2")
def mq2():
    if request.method == "GET":
        return render_template("mq2.html")

@app.route("/mq3")
def mq3():
    if request.method == "GET":
        return render_template("mq3.html")

@app.route("/mq4")
def mq4():
    if request.method == "GET":
        return render_template("mq4.html")

@app.route("/wash1")
def wash1():
    if request.method == "GET":
        return render_template("wash1.html")

@app.route("/wash2")
def wash2():
    if request.method == "GET":
        return render_template("wash2.html")

@app.route("/wash3")
def wash3():
    if request.method == "GET":
        return render_template("wash3.html")

@app.route("/wash4")
def wash4():
    if request.method == "GET":
        return render_template("wash4.html")

@app.route("/wash5")
def wash5():
    if request.method == "GET":
        return render_template("wash5.html")

@app.route("/wash6")
def wash6():
    if request.method == "GET":
        return render_template("wash6.html")

@app.route("/wash7")
def wash7():
    if request.method == "GET":
        return render_template("wash7.html")

@app.route("/wash8")
def wash8():
    if request.method == "GET":
        return render_template("wash8.html")

@app.route("/wash9")
def wash9():
    if request.method == "GET":
        return render_template("wash9.html")

@app.route("/wash10")
def wash10():
    if request.method == "GET":
        return render_template("wash10.html")

@app.route("/wash11")
def wash11():
    if request.method == "GET":
        return render_template("wash11.html")

@app.route("/wash12")
def wash12():
    if request.method == "GET":
        return render_template("wash12.html")

@app.route("/wash13")
def wash13():
    if request.method == "GET":
        return render_template("wash13.html")

@app.route("/wq1")
def wq1():
    if request.method == "GET":
        return render_template("wq1.html")

@app.route("/wq2")
def wq2():
    if request.method == "GET":
        return render_template("wq2.html")

@app.route("/wq3")
def wq3():
    if request.method == "GET":
        return render_template("wq3.html")

@app.route("/wq4")
def wq4():
    if request.method == "GET":
        return render_template("wq4.html")

@app.route("/wq5")
def wq5():
    if request.method == "GET":
        return render_template("wq5.html")
