from crypt import methods
from app import db
from app.models.breakfast import Breakfast
from flask import Blueprint, jsonify, abort, make_response, request
'''
class Breakfast():
    def __init__(self, id, name, rating, prep_time):
        self.id = id
        self.name = name
        self.rating = rating
        self.prep_time = prep_time

breakfast_items = [
    Breakfast(1, "omelet", 4, 10),
    Breakfast(2, "french toast", 3, 15),
    Breakfast(3, "cereal", 1, 1),
    Breakfast(4, "oatmeal", 3, 10),
    ]
'''
breakfast_bp = Blueprint("breakfast", __name__, url_prefix = "/breakfast")

@breakfast_bp.route("", methods = ["GET"])
def get_all_breakfasts():
    result = [] 
    all_breakfasts = Breakfast.query.all()
    for item in all_breakfasts:
        item_dict = {
            "id": item.id, 
            "name": item.name,
            "rating": item.rating,
            "prep_time": item.prep_time
            }
        result.append(item_dict)
    return jsonify(result), 200
'''
def validate_breakfast(breakfast_id):
    try:
        breakfast_id = int(breakfast_id)
    except:
        abort(make_response({"message": f"breakfast {breakfast_id} invalid"}, 400))

    for breakfast in breakfast_items:
        if breakfast.id == breakfast_id:
            return breakfast

    abort(make_response({"message": f"breakfast {breakfast_id} not found"}, 404))

@breakfast_bp.route("/<breakfast_id>", methods = ["GET"])
def get_one_breakfast(breakfast_id):
    breakfast = validate_breakfast(breakfast_id)
    return {"id": breakfast.id,
            "name": breakfast.name,
            "rating": breakfast.rating,
            "prep time": breakfast.prep_time}
'''

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



