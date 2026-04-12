# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My App
# Flask is the hub that manages the routes to all the pages
app = Flask(__name__)

# Home page
# Route to home page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ in "__main__":
    app.run(debug=True)