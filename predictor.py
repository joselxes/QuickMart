from marketClass import *

def storeInventory():
    # These function will read each line and store in the market inventory
    data=Inventory()
    try:
        while True:
            newProd=Product(input().split())
            # print(newProd)
            data.addProduct(newProd)
            # print(data)
    except:
        return data
    # print(data)    

    return 0

def main():
    store=Inventory()

    store=storeInventory()
    print(store,1)
    # store.upDate("Milk",2)
    cart=Cart()
    cart.addItem("Red-Bull",2)
    cart.addItem("Milk",2)
    cart.addItem("Flour",1)
    receipt=cart.checkOut(store,True,20.00)
    cart.printReceipt(receipt)
    print(store,2)
    # print(cart)

main()


