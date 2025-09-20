from flask import Flask
from processor.worker import start_worker
start_worker()

app = Flask(__name__)

from routes import routes