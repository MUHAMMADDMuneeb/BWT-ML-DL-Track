import datetime

class FoodItem:
    def __init__(self,name,category,quantity,barcode,expiredate):
        self.name=name
        self.category=category
        self.quantity=quantity
        self.barcode=barcode
        self.expiredate=expiredate
    def __repr__(self):
        return f"FoodItem(name={self.name}, category={self.category}, quantity={self.quantity}, barcode={self.barcode}, expiry_date={self.expiredate})"
        
class Inventory:
    def __init__(self):
        self.items=[]
    def Add_Item(self,Food_Item):
        self.items.append(Food_Item)
    def Edit_Item(self,barcode,name=None,category=None,quantity=None,expiredate=None):
        for item in self.items:
            if item.barcode == barcode:
                if name is not None:
                    item.barcode=name
                if category is not None:
                    item.category=category
                if quantity is not None:
                    item.quantity=quantity
                if expiredate is not None:
                    item.expiredate=expiredate
            return True
        return False
    def Search_Item(self,barcode=None, name=None):
       results = []
       for item in self.items:
            if barcode is not None and item.barcode == barcode:
                results.append(item)
            elif name is not None and item.name.lower() == name.lower():
                results.append(item)
       return results
    
    def Delete_Item(self,barcode):
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                return True
        return False
    def Near_Expiry_Items(self, days=7):
        near_expiry = []
        current_date = datetime.date.today()
        for item in self.items:
            if item.expiredate - current_date <= datetime.timedelta(days=days):
                near_expiry.append(item)
        return near_expiry
    
    
if __name__ == "__main__":
    inventory = Inventory()
    
    item1 = FoodItem("Milk", "Dairy", 10, "123456", datetime.date(2024, 7, 10))
    item2 = FoodItem("Bread", "Bakery", 20, "789012", datetime.date(2024, 7, 15))
    item3 = FoodItem("Eggs", "Poultry", 30, "345678", datetime.date(2024, 7, 8))
    
    inventory.Add_Item(item1)
    inventory.Add_Item(item2)
    inventory.Add_Item(item3)
    
    print("All Items:", inventory.items)
    print("Search by Barcode:", inventory.Search_Item(barcode="123456"))
    print("Near Expiry Items:", inventory.Near_Expiry_Items())

    inventory.Edit_Item(barcode="123456", quantity=15)
    print("After Edit:", inventory.Search_Item(barcode="123456"))

    inventory.Delete_Item(barcode="345678")
    print("After Deletion:", inventory.items)
