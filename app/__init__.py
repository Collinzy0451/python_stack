from flask import Flask
from config import Config
import os



app = Flask(__name__)
app.config.from_object(Config)


app.config["SECRET_KEY"] = os.environ.get("MY_SECRET")

from app.route.admin import *
from app.route.user import *
from app.route.root import *
