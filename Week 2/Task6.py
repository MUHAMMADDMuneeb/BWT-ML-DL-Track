def update_inventory(inventory_dict, item, quantity,action):
    current_quantity = inventory_dict[item]
    if action == "+":
        new_quantity = current_quantity + quantity
    else:
        new_quantity = current_quantity - quantity
        
    # Ensure quantity doesn't go below zero
    if new_quantity < 0:
        new_quantity = 0
    
    inventory_dict[item] = new_quantity
    return inventory_dict

def main():
    # Initialize inventory dictionary
    inventory = {
        "Apple": 10,
        "Banana": 5,
        "Orange": 7,
        "Mango": 3,
        "Pineapple": 2
    }
    
    # Display initial inventory
    print("Initial Inventory:")
    print(inventory)
    
    # Prompt user to update inventory
    for _ in range(3):
        item = input("\nEnter item to update: ")
        action = input("Do you want to add (+) or remove (-) inventory? Enter + or -: ")
        quantity = int(input("Enter quantity: "))
        
        
        inventory = update_inventory(inventory, item, quantity,action)
        
      
    
    # Display updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

if __name__ == "__main__":
    main()
