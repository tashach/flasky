from crypt import methods
from app import db
from app.models.breakfast import Breakfast
from app.models.menu import Menu
from flask import Blueprint, jsonify, abort, make_response, request
from app.routes.breakfast import validate_model_id

menu_bp = Blueprint("menu", __name__, url_prefix = "/menu")

@menu_bp.route("", methods=["GET"])
def get_all_menus():
    menus = Menu.query.all()
    response_body = [menu.to_dict() for menu in menus]
    return jsonify(response_body), 200

@menu_bp.route("", methods=["POST"])
def create_menu():
    request_body = request.get_json()

    new_menu = Menu(restaurant_name = request_body.get("restaurant_name"),
                    meal = request_body.get("meal"))

    db.session.add(new_menu)
    db.session.commit()

    return jsonify(f"new menu {new_menu.restaurant_name} successfully created"), 201


@menu_bp.route("/<menu_id>", methods = ["GET"])
def get_one_menu(menu_id):
    chosen_menu = validate_model_id(Menu, menu_id)
    return jsonify(chosen_menu.to_dict())

@menu_bp.route("/<menu_id>/breakfasts", methods=["GET"])
def get_breakfasts_for_menu(menu_id):
    menu = validate_model_id(Menu, menu_id)

    breakfasts = menu.get_breakfast_list()

    return jsonify(breakfasts), 200
