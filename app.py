#!/usr/bin/python3
from flask import Flask, render_template, url_for
import dadjokes

app = Flask(__name__)

# THIS IS A LIIS OF DICT PAIRS WITH JOKES
REDDIT_JOKES = dadjokes.ALL_JOKES

POSTS = [
  {
    "id": 0,
    "post_date": "Today",
    "category": "Tech",
    "title":"How To Automate With Python",
    "description":"some randome text for the description",
    "subreddit":"dadjokes"

  },
  {
    "id": 1,
    "post_date": "Today",
    "category": "Tech",
    "title":"10 Best Practices for Implementing DevOps in Your Organization",
    "description":"This post will provide actionable tips on how to successfully implement DevOps in your organization, including tips for collaboration, automation, and monitoring",
    "subreddit":"dadjokes"

  },
  {
    "id": 2,
    "post_date": "Today",
    "category": "Tech",
    "title":"5 Common DevOps Mistakes and How to Avoid Them",
    "description":"This post will identify common mistakes made by organizations when implementing DevOps and provide tips on how to avoid them, including tips for culture, automation, and monitoring.",
    "subreddit":"dadjokes"
    
  }
]

# register app
@app.route("/")
def show_page():
  return render_template('index.html', posts=POSTS, jokes=REDDIT_JOKES)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
