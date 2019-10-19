from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.run(host='0.0.0.0')
