#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

POSTS = [
  {
    "id": 1,
    "title":"How To Automate With Python",
    "description":"some randome text for the description"
  }
]

# register app
@app.route("/")
def show_page():
  return render_template('index.html', posts=POSTS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
