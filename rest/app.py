from flask_restless import APIManager
from persistence import *

manager = APIManager(app, flask_sqlalchemy_db=db)
astronauts_blueprint_v1 = manager.create_api_blueprint(Astronauts, methods=['GET', 'POST', 'PATCH', 'DELETE'])
astronauts_blueprint_v2 = manager.create_api_blueprint(Astronauts2, collection_name='astronauts2', methods=['GET', 'POST', 'PATCH', 'DELETE'])
app.register_blueprint(astronauts_blueprint_v1)
app.register_blueprint(astronauts_blueprint_v2)
manager.create_api(Vehicles, methods=['GET', 'POST', 'PATCH', 'DELETE'])
manager.create_api(Evas, methods=['GET', 'POST', 'PATCH', 'DELETE'])

@app.route('/')
def index():
  return 'Hello from the Stars!'

