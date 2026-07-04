from app import app

def test_start_route():
     client = app.test_client()
     response = client.get("/")

     assert response.status_code == 200
     assert response.data.decode() == "Welcome,Inventory-Management-System is Running"

