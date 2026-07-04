from unittest.mock import patch,Mock
from services import fetch_product_by_barcode
import requests

# If it is successful
@patch("services.requests.get")
def test_fetch_product_success(mock_get):
  mock_response = Mock()
  mock_response.raise_for_status.return_value = None
  mock_response.json.return_value = {
    "status": 1,
    "product": {
            "product_name": "Del-Monte Pineapple Juice 1L",
            "ingredients_text": "Water, Pineapple Juice Concentrate, Sugar, Vitamin C",
            "brands": "DELMONTE"
        }
  }

  mock_get.return_value = mock_response

  product = fetch_product_by_barcode("5449000131805")

  assert product["product_name"] == "Del-Monte Pineapple Juice 1L"
  assert product["brand"] == "DELMONTE"

# If Product doesnt exist
@patch("services.requests.get")
def test_fetch_product_not_found(mock_get):
    mock_response = Mock()

    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        "status": 0
    }

    mock_get.return_value = mock_response

    product = fetch_product_by_barcode("999999")

    assert product is None

# If Network Error
@patch("services.requests.get")
def test_fetch_product_network_error(mock_get):
   mock_get.side_effect = requests.RequestException

   product = fetch_product_by_barcode("5449000131805")
   assert product is None