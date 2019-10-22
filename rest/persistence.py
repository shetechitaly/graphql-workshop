from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

evas_crews = db.Table('evas_crews',
    db.Column('astronaut_id', db.Integer, db.ForeignKey('astronauts.id'), primary_key=True),
    db.Column('eva_id', db.Integer, db.ForeignKey('evas.id'), primary_key=True)
)

class Astronauts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  evas = db.relationship(
        "Evas",
        secondary=evas_crews,
        back_populates="astronauts")

  def __init__(self, name):
    self.name = name
    

class Astronauts2(Astronauts):
  country = db.Column(db.String(10))

  def __init__(self, name):
    self.name = name
    self.country = country
    

class Vehicles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  evas = db.relationship("Evas", back_populates="vehicle")

  def __init__(self, name):
    self.name = name


class Evas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  eva_date = db.Column(db.Date)
  duration = db.Column(db.Interval)
  purpose = db.Column(db.Text)
  vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
  vehicle = db.relationship("Vehicles", back_populates='evas')
  astronauts = db.relationship(
        "Astronauts",
        secondary=evas_crews,
        back_populates="evas")


  def __init__(self, eva_date, duration, purpose):
    self.eva_date = eva_date
    self.duration = duration
    self.purpose = purpose
 
