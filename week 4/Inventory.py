import datetime
import csv

class FileHandler:
    def __init__(self, filename='F:/Bitwise ML DL Intership/BWT-ML-DL-Track/week 4/inventory.csv'):
        self.filename = filename

    def load_from_file(self):
        items = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # skip empty rows
                        name, category, quantity, barcode, expiry_date = row
                        expiry_date = datetime.datetime.strptime(expiry_date, '%Y-%m-%d').date()
                        items.append(FoodItem(name, category, int(quantity), barcode, expiry_date))
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading from file: {e}")
        return items

    def save_to_file(self, items):
        try:
            print("Save to cALL")
            with open("F:/Bitwise ML DL Intership/BWT-ML-DL-Track/week 4/Output.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                for item in items:
                    print(item)
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiredate])
        except Exception as e:
            print(f"Error saving to file: {e}")


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
    def __init__(self,file_handler):
        self.items=[]
        self.file_handler=file_handler
        self.items=self.file_handler.load_from_file()
        
        
    def Add_Item(self,Food_Item):
        self.items.append(Food_Item)
        self.file_handler.save_to_file(self.items)
        
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
                self.file_handler.save_to_file(self.items)
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
                self.file_handler.save_to_file(self.items)
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
    file_handler=FileHandler()
    inventory = Inventory(file_handler)
    
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
    
   
