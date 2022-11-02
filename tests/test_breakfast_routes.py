def test_get_all_breakfasts_with_empty_db_returns_empty_list(client):
    response = client.get("/breakfast")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_breakfast_with_empty_db_returns_404(client):
    response = client.get("/breakfast/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "breakfast 1 not found"}

def test_get_one_breakfast_with_populated_db_returns_breakfast_json(client, two_saved_breakfasts):
    response = client.get("/breakfast/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "omelette",
        "rating": 6,
        "prep_time": 6
        }

def test_post_one_breakfast_creates_breakfast_in_db(client, two_saved_breakfasts):
    response = client.post("/breakfast", json = {
        "name": "pancakes",
        "rating": 10,
        "prep_time": 20
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {"msg": "Successfully created Breakfast with id = 3"}