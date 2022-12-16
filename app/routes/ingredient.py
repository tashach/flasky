from crypt import methods
from app import db
from app.models.breakfast import Breakfast
from app.models.menu import Menu
from app.models.ingredient import Ingredient
from flask import Blueprint, jsonify, abort, make_response, request
from app.routes.breakfast import validate_model_id

ingredient_bp = Blueprint("ingredient", __name__, url_prefix = "/ingredients")




