from flask import Blueprint, jsonify

class Potato:
    def __init__(self, name):
        self.name = name

my_potatoes = [Potato("yukon"), Potato("russet"), Potato("kennebec")]

potato_bp = Blueprint("potatoes", __name__, url_prefix="/potatoes")

@potato_bp.route('', methods=['GET'])
def get_potatoes():
    response = []
    id = 0
    for potato in my_potatoes:
        id += 1
        response.append({"id":id, "name":potato.name})
    
    return jsonify(response), 200

