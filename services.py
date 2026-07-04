import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"

# Fetch product info from OpenFoodFact using a barcode
def fetch_products_by_barcode(barcode):
  url = f"{BASE_URL}/{barcode}.json"

  response = requests.get(url, timeout=10)
  
  # check if the fetching is successful
  if response.status_code != 200:
    return None
  
  # check data status from openfood facts should not be 0
  data = response.json()
  if data.get("status") != 1:
    return None
  
  # Return only what's needed
  product = data["product"]
  return {
    "product_name":product.get("product_name"),
    "brand":product.get("brands"),
    "ingredients_text":product.get("ingredients_text")

  }