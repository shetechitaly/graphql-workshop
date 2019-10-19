from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Astronauts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))

  def __init__(self, name):
    self.name = name

  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/astronauts')
def astronauts():
  return jsonify([a.as_dict() for a in Astronauts.query.all()])

@app.route('/astronauts/<int:astronaut_id>')
def astronaut(astronaut_id):
  return str(astronaut_id)
