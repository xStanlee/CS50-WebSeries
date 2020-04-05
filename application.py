import os
import requests

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure sqlalchemy to connect my DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Request for jsonFile
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "cIAWnULXTSoqvTIKqOMdTQ", "isbns": "9781632168146"})
resJson = res.json()

class Book:
    def __init__(self, title, author, year, isbn, review_count, avarge_score):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.review_count = review_count
        self.avarge_score = avarge_score
class User:
    def __init__(self, first_name, last_name, username, password, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

@app.route("/")
def login():
    awatar = Book('Awatar', 'JakisDzonson', 1994, 23212321, 42, 4.11)
    return render_template('login.html', title="Login page")

@app.route("/registration/")
def registration():
    return render_template('registration.html', title="Registration page")