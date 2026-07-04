from flask import current_app
from flask import jsonify
from inventory import inventory

def register_endponts(app):
  @app.route("/")
  def start():
      return f"Welcome,Inventory-Management-System is Running"
  
  # getting all items from the inventory
  @app.get("/inventory")
  def get_inventory():
     return jsonify(inventory), 200
  
  # getting specific item
  @app.get("/inventory/<int:item_id>")
  def get_inventory_item(item_id):
      for item in inventory:
        if item["id"] == item_id:
           return jsonify(item), 200

      return jsonify({"error":"Inventory Item not Found"}), 404
  
    
     
     