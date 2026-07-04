"""
Mock inventory database.
This module simulates a database by storing inventory items in a Python
list. Each inventory item is represented as a dictionary.
"""

inventory = [
    {
        "id": 1,
        "barcode": "45638809",
        "price": 200.00,
        "stock": 50,
        "supplier": "KCC Milk Limited",
        "product_details": {
            "product_name": "5L Fermented Milk",
            "ingredients_text": "Milk, Citric Acid, Milk Powder",
            "brand": "Cows' Milk"
        }
    },
    {
        "id": 2,
        "barcode": "9780201379624",
        "price": 650.00,
        "stock": 30,
        "supplier": "Dormans Coffee Ltd",
        "product_details": {
            "product_name": "Ground Coffee 500g",
            "ingredients_text": "Ground Arabica Coffee",
            "brand": "Dormans"
        }
    },
    {
        "id": 3,
        "barcode": "7622210449283",
        "price": 180.00,
        "stock": 120,
        "supplier": "Mumias Kenya Sugar Company",
        "product_details": {
            "product_name": "Brown Sugar 2kg",
            "ingredients_text": "Refined Cane Sugar",
            "brand": "Kabras Sugar"
        }
    },
    {
        "id": 4,
        "barcode": "5901234123457",
        "price": 170.00,
        "stock": 95,
        "supplier": "Unga Limited",
        "product_details": {
            "product_name": "Maize Flour 2kg",
            "ingredients_text": "Fortified Maize Flour",
            "brand": "Jogoo"
        }
    },
    {
        "id": 5,
        "barcode": "8938501434012",
        "price": 350.00,
        "stock": 70,
        "supplier": "Mwea Kenya Distributors",
        "product_details": {
            "product_name": "Basmati Rice 2kg",
            "ingredients_text": "Premium Basmati Rice",
            "brand": "Pulse"
        }
    },
    {
        "id": 6,
        "barcode": "5449000131805",
        "price": 120.00,
        "stock": 85,
        "supplier": "Coca-Cola Beverages Africa",
        "product": {
            "product_name": "Del-Monte Pineapple Juice 1L",
            "ingredients_text": "Water, Pineapple Juice Concentrate, Sugar, Vitamin C",
            "brand": "DELMONTE"
        }
    }
]

