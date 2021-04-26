import os
from flask import url_for

class Config:
    # App
    try:
        SECRET_KEY = os.environ['SECRET_KEY']
    except:
        SECRET_KEY = 'test'
    DEBUG = True

    # Database Stuff
    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/vedantatrivedi/Downloads/tarp/flaskapp/health.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_PATH = 'flaskapp/static/template/build/static'