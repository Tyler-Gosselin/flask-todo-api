import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
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
    return todo_schema.jsonify(new_todo)

# Get all the Todos


@app.route('/api/get-all-todos', methods=['GET'])
def get_all_todos():
    all_todos = Todo.query.all()
    return jsonify(todos_schema.dump(all_todos))


# Edit a Todo's "done" field
@app.route('/api/edit-done/<todo_id>', methods=['PATCH'])
def edit_done(todo_id):
    todo = Todo.query.get(todo_id)
    new_done = request.json['done']
    todo.done = new_done
    db.session.commit()
    return todo_schema.jsonify(todo)

# Delete a todo


@app.route('/api/delete-todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return "Todo Deleted!"


if __name__ == "__main__":
    app.debug = True
    app.run()
