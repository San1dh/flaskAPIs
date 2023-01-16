from flask import Flask, request, render_template

from helpers import get_date_and_time

app = Flask(__name__)

@app.route("/")
def homepage():
    return("hello world")

if __name__ == "__main__":
    app.run(debug = True)