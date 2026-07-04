from inventory import inventory

# inventory should be a list
def test_inventory_is_a_list():
  assert isinstance(inventory,list)

# Inventory should contain atleast one list
def test_inventory_contains_one_product():
  assert len(inventory) >= 1
