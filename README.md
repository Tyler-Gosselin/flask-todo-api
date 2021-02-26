# Flask Todo Api
## Dependency Docs
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
- [flask-cors](https://flask-cors.readthedocs.io/en/latest/)
## How to start the server
```
$ pipenv shell
$ python app.py
```
## How to create the database
```
$ pipenv shell
$ python
>>> from app import db
>>> db.create_all()
```
## Routes
### Create a single todo:
```json
{
  "method": "POST",
  "url": "http://localhost:5000/api/add-todo",
  "body": {
    "title": "Learn how to program",
    "done": false
  },
  "Content-Type": "application/json"
}
```
### Get all todos:
```json
{
  "method": "GET",
  "url": "http://localhost:5000/api/get-all-todos"
}
```
### Edit a single todos:
```json
{
  "method": "PATCH",
  "url": "http://localhost:5000/api/edit-done/TODO_ID",
  "body": {
    "done": true
  },
  "Content-Type": "application/json"
}
```
### Delete a single todo:
```json
{
  "method": "DELETE",
  "url": "http://localhost:5000/api/delete-todo/TODO_ID",
}
```