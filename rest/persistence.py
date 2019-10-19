from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Astronauts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  country = db.Column(db.String(10))
  vehicles = db.relationship(
        "Vehicles",
        secondary=eva_crews,
        back_populates="astronauts")
  evas = db.relationship(
        "Evas",
        secondary=eva_crews,
        back_populates="astronaut")

  def __init__(self, name, country):
    self.name = name
    self.country = country
    

class Vehicles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  astronauts = db.relationship("Astronauts", secondary=eva_crews, back_populates="vehicles")
  evas = db.relationship(
        "Evas",
        secondary=eva_crews,
        back_populates="vehicle")

  def __init__(self, name):
    self.name = name


class Evas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration = db.Column(db.Interval)
  purpose = db.Column(db.Text)
    evas = db.relationship(
        "Evas",
        secondary=eva_crews,
        back_populates="vehicle")


  def __init__(self, date, duration, purpose):
    self.date = date
    self.duration = duration
    self.purpose = purpose
 