# Jerry's Quick Mart
interview assignment
Developed in Linux python3 
 
-to run a stressTest run the command "pthon3 quickMart.py", and follow the intructions.


## marketClass.py 
Contains the 3 Classes.
### class Product
Has all details of the product, such as:
    -Name of the product
    -Quantity available in the store.
    -Product's price for member.
    -Product's price for no members.
    -And an integer, 1 if the product is Tax-exempt or 0 if it is Taxable.


### Inventory 
The attributes of this class are:
    -inventory as a dictionary to store the products.
    -the number of transactions performed in the store

Has two basic functions:
    -addProduct() which adds a product to the inventory dictionary.
    -increasetransactions() count the number of finished trasactions.
    -upDate() which helps to update the quantity of each product that the store has.
    


### Cart 
The attributes are:
    -items is a dictionary to store the items added to the cart.
    -subtotal,tax,total,change,saved are variables to generate the receipt.
    -receipt is a list that saves multiple strings, used to print the receipt.


Functions:
    -listItems() return a list with the keys of the dictionary from the attribute items.
    -addItem() adds a product to the attribute items.
    -removeItem() reduce the quantity of a product or removes it. 
    -empty() return True if the cart is empty otherwise False.
    -checkOut() calculates the different values to perform the transaction.
    -printReceipt() Saves the receipt in a .txt file.
    -
    -