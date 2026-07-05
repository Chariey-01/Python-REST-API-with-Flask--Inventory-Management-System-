from app import app
from unittest.mock import patch

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

 # Successful Post
@patch("routes.fetch_product_by_barcode")
def test_add_inventory_item_suceess(mock_fetch):
    mock_fetch.return_value = {
          "product_name": "Orange Juice",
          "brand": "Minute Maid",
          "ingredients_text": "Water, Orange Juice Concentrate"
    }
    
    client = app.test_client()
    response = client.post(
    "/inventory",
    json={
        "barcode": "5449000131805",
        "price": 180,
        "stock": 40,
        "supplier": "Coca-Cola Beverages Africa"
    }
)
    assert response.status_code == 201

    data = response.get_json()

    assert data["barcode"] == "5449000131805"
    assert data["price"] == 180
    assert data["stock"] == 40
    assert data["supplier"] == "Coca-Cola Beverages Africa"
    assert data["product_details"]["product_name"] == "Orange Juice"

# required field missing
def test_add_inventory_missing_supplier():
    client = app.test_client()

    response = client.post(
        "/inventory",
        json={
            "barcode": "5449000131805",
            "price": 180,
            "stock": 40
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data    

# Barcode not found
@patch("routes.fetch_product_by_barcode")
def test_add_inventory_item_not_found(mock_fetch):
    mock_fetch.return_value = None

    client = app.test_client()

    response = client.post(
        "/inventory",
        json={
            "barcode": "000000",
            "price": 180,
            "stock": 40,
            "supplier": "Unknown Supplier"
        }
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Product not found in OpenFoodFacts."

# patch test success
def test_patch_inventory_success():
    client = app.test_client()

    response = client.patch(
        "/inventory/1",
        json={
            "price": 250,
            "stock": 75
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["price"] == 250
    assert data["stock"] == 75

# Non existing item during patch
def test_patch_inventory_not_found():
    client = app.test_client()

    response = client.patch(
        "/inventory/999",
        json={
            "price": 250
        }
    )

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Inventory item not found."

# igonore protected field during patchind
def test_patch_ignores_protected_fields():
    client = app.test_client()

    response = client.patch(
        "/inventory/1",
        json={
            "id": 99,
            "barcode": "111111111111",
            "price": 300
        }
    )

    data = response.get_json()

    assert response.status_code == 200

    assert data["id"] == 1
    assert data["barcode"] == "45638809"
    assert data["price"] == 300

# successful delete
def test_delete_inventory_success():
    client = app.test_client()

    response = client.delete("/inventory/6")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Inventory item deleted successfully."
    assert data["deleted_item"]["id"] == 6

# delete product doest exist
def test_delete_inventory_not_found():
    client = app.test_client()

    response = client.delete("/inventory/999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Inventory item not found."
    

