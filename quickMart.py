from marketClass import *

def addToCart(store,cart):
    addMore=""
    itemIndex=0
    print("-------------- \n")
    itemsStorage=store.listProducts()
    for i in range(0,len(itemsStorage)):
        print(str(i+1)+".-",itemsStorage[i])
    print("-------------- \n")
    print("""Introduce the number of the product that you want to ADD, or "no" to go back to the main menu:""")
    addMore=input()
    while not(addMore in ["n","no","N","NO"]):
        if int(addMore)>len(itemsStorage):
            print("error item does not exist!!")        
        else:
            print("Selected=>",itemsStorage[int(addMore)-1])
            print("Introduce the quantity of "+itemsStorage[int(addMore)-1].upper()+" that you want:")
            itemQuantity=int(input())

            try:
                cart.addItem(itemsStorage[int(addMore)-1],itemQuantity)
                print("Added:",itemsStorage[int(addMore)-1],"(",itemQuantity,")")
            except:
                print("An error ocurred while trying add the product.")
        print("""Add another product introducing the index, or "no" to go back to the main menu:""")
        addMore=input()
    return True

def deleteFromCart(cart):
    addMore=""
    itemIndex=0
    print("-------------- YOUR CART HAS: \n")
    itemsStorage=cart.listItems()
    print(cart)    

    print("""Introduce the number of the product that you want to REMOVE, or "no" to go back to the main menu:""")
    addMore=input()
    while not(  (addMore in ["n","no","N","NO"]) or  len(itemsStorage)==0):
        if int(addMore)>len(itemsStorage):
            print("error item does not exist!!")        
        else:
            print("Selected=>",itemsStorage[int(addMore)-1])
            print("Introduce the quantity that yo want to remove "+itemsStorage[int(addMore)-1].upper()+" that you want:")
            itemQuantity=int(input())

            try:
                cart.removeItem(itemsStorage[int(addMore)-1],itemQuantity)
                print("----The item:",itemsStorage[int(addMore)-1],"(",itemQuantity,")")
                print(cart)
                itemsStorage=cart.listItems()
            except:
                print("An error ocurred while trying add the product.")
        print(itemsStorage,len(itemsStorage))
        if len(itemsStorage)>0:
            print("""Remove or another product introducing the index, or "no" to go back to the main menu:""")
            addMore=input()

    return True

def storeInventory(file):
    # These function will read each line and store in the market inventory
    data=Inventory()
    text=open(file,"r")
    a=0
    for line in text:
        a+=1
        linea=line.split()
        newProd=Product(linea)
        print(newProd)
        data.addProduct(newProd)
    text.close()        
    return data
    # try:
    #     text=open(file,"r")
    #     a=0
    #     for line in text:
    #         a+=1
    #         linea=line.split()
    #         newProd=Product(linea)
    #         print(newProd)
    #         data.addProduct(newProd)
    #     text.close()        
    #     return data
    # except:
    #     print("The format used, is not correct.")
    # print(data)    

    return 0

def viewCart(cart,store,member):
    print(cart)
    print("Introduce the amount used to pay: ")
    cash=float(input())
    details=cart.checkOut(store,member,cash,True)
    for i in details[1]:
        print(i)
    # print(details)
    return False


def main():
    store=Inventory()

    # store=storeInventory("inventory.txt")
    store=storeInventory("inventory.txt")
    cart=Cart()
    member=False
    loggin=False
    run=True
    while (run):
        try:
            if loggin==False:
                print("""Are you a  Reward member type "yes" if you are, otherwise type "no":""")
                reward=input()
                cart=Cart()
                if reward in["yes","y","YES","Y"]:
                    print("\n\t----Welcome dear member----")
                    cart.member=True
                    member=True
                else:
                    print("\n\t----Welcome dear costumer----")
                    member=False
                loggin=True
            print("\nYour car is empty:\n")
            print("""1.- Type "1" if you want to see the available products.\n""")
            print("""2.- Type "2" if you want to add a product.\n""" )
            if cart.empty():
                pass
                # print("""Type "3" if you want to""")
            else:
                print("""3.-Type "3" if you want to delete a product of your car.\n""")
            print("""4.- Type "4" if you want view your cart.\n""")
            print("""5.- Type "5" if you want to checkout and exit.\n""")
            print("""5.- Type "6" if you want to cancel the transaction and exit.\n""")
            option=input()
            """ option 1 on show """

            if option=="1":
                print(store)

            """ option 2 add items to cart  """
            if option=="2":
                addToCart(store,cart)

            """ option 3 remove items from the cart, if car is empty nothing to remove  """
            if not cart.empty():
                if option=="3":
                    deleteFromCart(cart)
            """ option 4 allow view cart incluiding totals  """
            if option=="4":
                viewCart(cart,store,member)
            """ option 5 checkout and print receipt  """
            if option=="5":
                print("Introduce the amount used to pay: ")
                cash=float(input())
                receiptName,receiptText=cart.checkOut(store,member,cash,False)
                cart.printReceipt(receiptName,receiptText)            
                loggin=False
                print("\n""\n""\n""\n""\n""----------------------")

                print(store)
            """ option 6 cancel transaction  """
            if option=="6":
                print(bye)
                loggin=False
                run=False
        except:
            print("bye")
            run=False




main()


