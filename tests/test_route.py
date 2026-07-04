from app import app

# Test for the getall route
def test_get_inventory():
    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 6

# Testing Exixsting product
def test_get_single_inventory_item():
    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1 

# Testing missing Product
def test_get_nonexistent_inventory_item():
    client = app.test_client()

    response = client.get("/inventory/100")

    assert response.status_code == 404

    data = response.get_json()

    assert "error" in data
