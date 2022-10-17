from flask import Blueprint, jsonify

class Potato:
    def __init__(self, name, id):
        self.name = name
        self.id = id

my_potatoes = [Potato("yukon", 1), Potato("russet", 2), Potato("kennebec", 3)]

potato_bp = Blueprint("potatoes", __name__, url_prefix="/potatoes")

@potato_bp.route('', methods=['GET'])
def get_potatoes():
    response = []
    for potato in my_potatoes:
        response.append({"id":potato.id, "name":potato.name})
    
    return jsonify(response), 200

@potato_bp.route('/<potato_id>', methods=['GET']) #methods with an s
def get_one_potato(potato_id): #match names
    try:
        potato_id = int(potato_id)
    except ValueError:
        return {
            'msg': f'invalid input: {potato_id}'
        }, 400
    found_potato = None
    for potato in my_potatoes:
        if potato.id == potato_id:
            found_potato = potato
            break
    
    if found_potato is None:
        return {
            'msg': f'Could not find potato: {potato_id}'
        }, 404
    return {
        'id': found_potato.id,
        'name': found_potato.name
    }, 200
