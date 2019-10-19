from flask import jsonify
from persistence import *


@app.route('/')
def index():
  return 'Hello from the Stars!'
  
@app.route('/astronauts')
def astronauts():
  return jsonify([a.as_dict() for a in Astronauts.query.all()])

@app.route('/astronauts/<int:astronaut_id>')
def astronaut(astronaut_id):
  return jsonify(Astronauts.query.filter_by(id=astronaut_id).first().as_dict())
