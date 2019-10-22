from flask_restless import APIManager
from persistence import *

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Astronauts, methods=['GET', 'POST', 'PATCH', 'DELETE'])
manager.create_api(Vehicles, methods=['GET', 'POST', 'PATCH', 'DELETE'])
manager.create_api(Evas, methods=['GET', 'POST', 'PATCH', 'DELETE'])

@app.route('/')
def index():
  return 'Hello from the Stars!'

