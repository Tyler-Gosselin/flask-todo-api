import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "app.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean)

    def __init__(self, title, done):
        self.title = title
        self.done = done


class TodoSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "done")


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


@app.route('/')
def hello():
    return "Hello World!"


# Create a Todo
@app.route('/api/add-todo', methods=['POST'])
def add_todo():
    title = request.json['title']
    done = request.json['done']
    new_todo = Todo(title, done)
    db.session.add(new_todo)
    db.session.commit()
    todo = Todo.query.get(new_todo.id)
    print(todo)
    print(todo_schema.jsonify(todo))
    return todo_schema.jsonify(todo)

# Get all the Todos

# Edit a Todo's "done" field

# Delete a todo


if __name__ == "__main__":
    app.debug = True
    app.run()
