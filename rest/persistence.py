from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

def dictionarify():

    def as_dict(self):
      import pdb
      pdb.set_trace()
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def wrapper(K):
        setattr(K, "as_dict", as_dict)
        return K
    return wrapper

eva_crews = db.Table('evas_crews',
    db.Column('astronaut_id', db.Integer, db.ForeignKey('astronauts.id'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'), primary_key=True),
    db.Column('eva_id', db.Integer, db.ForeignKey('ebas.id'), primary_key=True)
)

@dictionarify()
class Astronauts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  country = db.Column(db.String(10))
  vehicles = db.relationship(
        "Vehicles",
        secondary=eva_crews,
        back_populates="astronauts")

  def __init__(self, name, country):
    self.name = name
    self.country = country
    

@dictionarify()
class Vehicles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  astronauts = db.relationship("Astronauts", secondary=eva_crews, back_populates="vehicles")

  def __init__(self, name):
    self.name = name


@dictionarify()
class Evas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration = db.Column(db.Interval)
  purpose = db.Column(db.Text)


  def __init__(self, date, duration, purpose):
    self.date = date
    self.duration = duration
    self.purpose = purpose
 