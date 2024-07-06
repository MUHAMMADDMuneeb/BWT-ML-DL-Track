# Inventory Management System
First of all it will take the data of Inventory from the Inventory.csv file and create the <br>
item of each row that is present.
<br><br>
Add Items: <br>

To add an item, provide details like name, category, quantity, barcode, and expiry date. Use the add_item function to add it to the inventory.<br>
Edit Items: <br>

To edit an item, provide the barcode and new details. Use the edit_item function to update the item.
Delete Items<br>
Delete Items:<br>
To delete an item, provide its barcode and use the delete_item function to remove it from the inventory.
<br>
Search Items:<br>
To search for items, use the search_item function with the barcode, name, or category.
Iterate Through Items: <br>

Use a for-loop to iterate through all items in the inventory.<br>
Find Near Expiry Items:<br>

Use the near_expiry_generator function to get items that are nearing their expiry date.
<br>Generate Reports: <br>

Use functions like generate_report_near_expiry, generate_report_low_stock, and generate_category_summary to create various reports based on inventory data.

<br>
Output: <br>
At Last it will enter the inventory data to Output.csv file