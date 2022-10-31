from crypt import methods
from app import db
from app.models.breakfast import Breakfast
from flask import Blueprint, jsonify, abort, make_response, request

breakfast_bp = Blueprint("breakfast", __name__, url_prefix = "/breakfast")

@breakfast_bp.route("", methods = ["GET"])
def get_all_breakfasts():
    result = [] 
    all_breakfasts = Breakfast.query.all()
    for item in all_breakfasts:
        result.append(item.to_dict())
    return jsonify(result), 200

@breakfast_bp.route("", methods = ["POST"])
def create_one_breakfast():
    request_body = request.get_json()
    new_breakfast = Breakfast(
        name = request_body['name'],
        rating = request_body['rating'],
        prep_time = request_body['prep_time']
    )
    db.session.add(new_breakfast)
    db.session.commit()

    return make_response("msg: "f"Successfully created Breakfast with id = {new_breakfast.id}", 201)

@breakfast_bp.route("/<breakfast_id>", methods = ["GET"])
def get_one_breakfast(breakfast_id):
    chosen_breakfast = validate_breakfast(breakfast_id)
    return jsonify(chosen_breakfast.to_dict())

def validate_breakfast(breakfast_id):
    try:
        breakfast_id = int(breakfast_id)
    except: 
        abort(make_response({"message": f"breakfast {breakfast_id} not found"}, 400))

    chosen_breakfast = Breakfast.query.get(breakfast_id)
    if not chosen_breakfast:
        abort(make_response({"message": f"breakfast {breakfast_id} not found"}, 404))
    return chosen_breakfast

