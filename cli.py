import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("\n===== Inventory Management System =====")
    print("1. View all products")
    print("2. View product by ID")
    print("3. Add product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Search product by barcode")
    print("0. Exit")


def view_inventory():
    # Retrieve and display all inventory items
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        print(response.json())
    else:
        print("Unable to retrieve inventory.")


def view_product():
    # Retrieve one product by ID
    item_id = input("Enter product ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print(response.json())
    else:
        print("Product not found.")


def add_product():
    # Add a new inventory item
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    supplier = input("Supplier: ")

    payload = {
        "barcode": barcode,
        "price": price,
        "stock": stock,
        "supplier": supplier
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=payload
    )

    print(response.json())


def update_product():
    # Update an existing inventory item
    item_id = input("Enter product ID: ")

    payload = {}

    price = input("New price (leave blank to skip): ")
    if price:
        payload["price"] = float(price)

    stock = input("New stock (leave blank to skip): ")
    if stock:
        payload["stock"] = int(stock)

    supplier = input("New supplier (leave blank to skip): ")
    if supplier:
        payload["supplier"] = supplier

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=payload
    )

    print(response.json())


def delete_product():
  # Delete an inventory item
    item_id = input("Enter product ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    print(response.json())


def search_product():
  # Search the foodfacts with using a barcode
    barcode = input("Enter barcode: ")

    response = requests.get(
        f"{BASE_URL}/product/{barcode}"
    )

    print(response.json())


def main():
    while True:
        menu()

        choice = input("\nSelect an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_product()

        elif choice == "3":
            add_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            search_product()

        elif choice == "0":
            print("Goodbye,Ciao,Adios...")
            break

        else:
            print("Invalid option, Try again.")


if __name__ == "__main__":
    main()