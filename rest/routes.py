from flask_restless import APIManager
from app import app
from persistence import *

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Astronauts)
manager.create_api(Vehicles)
manager.create_api(Evas)

@app.route('/')
def index():
  return 'Hello from the Stars!'

