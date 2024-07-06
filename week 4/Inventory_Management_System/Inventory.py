from .FoodItem import FoodItem
from .FileManager import FileHandler

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