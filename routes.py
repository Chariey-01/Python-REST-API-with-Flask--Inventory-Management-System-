from flask import current_app
from flask import jsonify,request
from inventory import inventory
from services import fetch_product_by_barcode

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
  
  # Post/creating new product/item to the list
  @app.post("/inventory")
  def add_inventory_item():
     data = request.get_json()
    #  validating expected input field
     input_fields = ["barcode","price","stock","supplier"]
     for field in input_fields:
        if field not in data:
           return jsonify({
              "error":f"'{field}' is required!."
           }), 400
      # error message for None
     product = fetch_product_by_barcode(data["barcode"])
     if product is None:
        return jsonify({
           "error":"Product not found in OpenFoodFacts"
        }), 404
     
     new_id = max((item["id"] for item in inventory),default=0) + 1
     new_item = {
    "id": new_id,
    "barcode": data["barcode"],
    "price": data["price"],
    "stock": data["stock"],
    "supplier": data["supplier"],
    "product_details": product
}
  # save the posted item 
     inventory.append(new_item)
     return jsonify(new_item),201
  
# Patching the items
  @app.patch("/inventory/<int:item_id>")
  def update_inventory_item(item_id):
   data = request.get_json()

   allowed_fields = ["price","supplier","stock"]
   for item in inventory:
      if item["id"] == item_id:
         for field in allowed_fields:
            if field in data:
               item[field] = data[field]
         return jsonify(item), 200    
   return jsonify({"error":"Inventory item not found"}), 404
   

     
     