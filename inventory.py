"""
this is a mock database for inventory storage and it stores items as a
 python list and every item is stored as a dictonary
"""
inventory = [{
  "id":1,
  "barcode": "45638809",
  "price": 200.00,
  "stock": 50,
  "supplier":"KCC milk limited",
  "product":{
    "product_name": "5L Fermented Milk",
    "ingredients_text":"Milk,citricAcid,milkPowder",
    "brand": "Cows' Milk"
  }
  
}]

