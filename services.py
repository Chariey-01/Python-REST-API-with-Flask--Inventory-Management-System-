import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"


def fetch_product_by_barcode(barcode):
    """
    Retrieve product details from OpenFoodFacts using a barcode.

    Returns:
        dict: Product information if found.
        None: If the product cannot be retrieved.
    """

    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data["product"]

        return {
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "ingredients_text": product.get("ingredients_text")
        }

    except requests.RequestException:
        return None