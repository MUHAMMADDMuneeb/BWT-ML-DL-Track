import datetime
import csv
from Inventory_Management_System import Inventory
from Inventory_Management_System import FileHandler
from Inventory_Management_System import FoodItem




if __name__ == "__main__":
    file_handler = FileHandler()
    inventory = Inventory(file_handler)

    # Adding items to the inventory
    item1 = FoodItem("Cheese", "Dairy", 15, "654321", datetime.date(2024, 8, 1))
    item2 = FoodItem("Chicken", "Meat", 25, "987654", datetime.date(2024, 7, 12))
    item3 = FoodItem("Apples", "Fruit", 50, "321654", datetime.date(2024, 7, 20))
    item4 = FoodItem("Bananas", "Fruit", 45, "654987", datetime.date(2024, 7, 18))
    item5 = FoodItem("Tomatoes", "Vegetable", 35, "789654", datetime.date(2024, 7, 14))

    inventory.Add_Item(item1)
    inventory.Add_Item(item2)
    inventory.Add_Item(item3)
    inventory.Add_Item(item4)
    inventory.Add_Item(item5)

    # Using the iterator to iterate through items
    print("All items in inventory:")
    for item in inventory:
        print(item)

    # Using the generator to get near expiry items
    print("\nItems nearing expiry:")
    for item in inventory.near_expiry_generator(days=7):
        print(item)
