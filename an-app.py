from flask import Flask, render_template

app = Flask(__name__)

# when a URL is requested, what is returned

# register app
@app.route("/")
def show_page():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
