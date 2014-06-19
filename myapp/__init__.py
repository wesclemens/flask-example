"""
This is the inital app setup
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache

__all__ = ['app', 'db', 'cache']

# Create Flask app for use as a global namespace
app = Flask(__name__, instance_relative_config=True)

# Load configs if exists
app.config.from_object('%s.config' % __name__)
app.config.from_pyfile('application.cfg', silent=True)

# Load flask extentions
cache = Cache(app)
db = SQLAlchemy(app)

# Load endpoints
import endpoint
