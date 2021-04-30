from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ggs/Desktop/todo_app/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    todolar = Todo.query.all()
    return render_template("index.htm", todolar=todolar)

@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title")
    newtodo = Todo(title=title, complete=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completetodo(id):
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deletetodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)