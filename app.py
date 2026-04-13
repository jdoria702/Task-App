# Imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# My App
# Flask is the hub that manages the routes to all the pages
app = Flask(__name__)
Scss(app)

# mandatory config key in Flask-SQLAlchemy
# tell application which database engine to use and where the database is located
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Model
# Data Class ~ Row of data
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    # To give data back to see on screen
    def __repr__(self) -> str:
        return f"Task {self.id}"

# Home page
# Route to home page
# Home page can add tasks and retrieve tasks
@app.route("/", methods=["POST", "GET"])
def index():
    # Add a Task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    # See all current tasks
    else:
        # Send tasks to HTML pages by accessing variable
        tasks = MyTask.query.order_by(MyTask.created).all()

        # tasks is a variable that jinja could use
        return render_template("index.html", tasks=tasks)
    


if __name__ in "__main__":
    # temporary workspace that keeps track of application-level data during a request, CLI command or other activity
    with app.app_context():
        db.create_all()

    app.run(debug=True)