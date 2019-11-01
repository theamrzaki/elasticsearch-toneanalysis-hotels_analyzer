from flask import Blueprint

hotel = Blueprint('hotel', __name__)

from . import routes
