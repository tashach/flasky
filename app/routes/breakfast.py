from crypt import methods
from app import db
from app.models.breakfast import Breakfast
# from app.models.breakfast_ingredient import BreakfastIngredient
# from app.models.ingredient import Ingredient
from flask import Blueprint, jsonify, abort, make_response, request

breakfast_bp = Blueprint("breakfast", __name__, url_prefix = "/breakfast")

@breakfast_bp.route("", methods = ["GET"])
def get_all_breakfasts():
    rating_query_value = request.args.get("rating")

    if rating_query_value is not None:
        breakfasts = Breakfast.query.filter_by(rating = rating_query_value)
    else:
        breakfasts = Breakfast.query.all()

    result = []
    for item in breakfasts:
        result.append(item.to_dict())

    return jsonify(result)

@breakfast_bp.route("", methods = ["POST"])
def create_one_breakfast():
    request_body = request.get_json()
    new_breakfast = Breakfast.from_dict(request_body)
    db.session.add(new_breakfast)
    db.session.commit()

    return jsonify({"msg": f"Successfully created Breakfast with id = {new_breakfast.id}"}), 201

@breakfast_bp.route("/<breakfast_id>", methods = ["GET"])
def get_one_breakfast(breakfast_id):
    chosen_breakfast = validate_model_id(Breakfast, breakfast_id)

    return jsonify(chosen_breakfast.to_dict())

@breakfast_bp.route("/<breakfast_id>", methods = ["PUT"])
def update_one_breakfast(breakfast_id):
    update_breakfast = validate_model_id(Breakfast, breakfast_id)
    request_body = request.get_json()

    try:
        update_breakfast.name = request_body["name"]
        update_breakfast.rating = request_body["rating"]
        update_breakfast.prep_time = request_body["prep_time"]
    except KeyError:
        return jsonify({"message": "Missing necessary information"}), 400

    db.session.commit()

    return jsonify(f"Breakfast {update_breakfast.name} successfully updated")

@breakfast_bp.route("/<breakfast_id>", methods = ["DELETE"])
def delete_one_breakfast(breakfast_id):
    breakfast_to_be_deleted = validate_model_id(Breakfast, breakfast_id)

    db.session.delete(breakfast_to_be_deleted)
    db.session.commit()

    return jsonify({"message": f"Successfully deleted breakfast {breakfast_to_be_deleted.name}"})

@breakfast_bp.route("/<breakfast_id>/<new_rating>", methods =["PATCH"])
def update_one_breakfast_rating(breakfast_id, new_rating):
    chosen_breakfast = validate_model_id(Breakfast, breakfast_id)

    try:
        new_rating = int(new_rating)
    except KeyError:
        return jsonify({"message": "Missing necessary information"}), 400

    db.session.commit()

    return jsonify(f"Breakfast rating successfully updated")



def validate_model_id(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        return abort(make_response({"message": f"invalid data type: {model_id}"}, 400))

    chosen_object = cls.query.get(model_id)

    if not chosen_object:
        return abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))

    return chosen_object

# @breakfast_bp.route('/<breakfast_id>', methods=['GET'])
# def get_ingredients_by_breakfast(breakfast_id):
#     breakfast = validate_model_id(Breakfast, breakfast_id)
#     ingredients = []
#     for ingredient in breakfast['ingredients']:
#         ingredients.append(ingredient.name)

#     return jsonify(ingredients), 200