from datetime import datetime
import calendar
import sys


class Product:
    def __init__(self,productDetails):
        self.prodName=productDetails[0][0:-1]
        self.quantity=int(productDetails[1][0:-1])
        self.priceNoMember=float(productDetails[2][1:-1])
        self.priceMember=float(productDetails[3][1:-1])

        if productDetails[4]=="Tax-Exempt":
            self.taxStatus=0
        else:
            self.taxStatus=1
    def __str__(self):

        nextItem=self.prodName+":"
        while len(nextItem)<11:
            nextItem+=" "
        if self.taxStatus:
            return f'{nextItem} \t{self.quantity}, \t${self.priceMember:.2}, \t${round(self.priceNoMember,2)},\t Taxable'       
        return f'{nextItem} \t{self.quantity}, \t${self.priceMember:.2}, \t${round(self.priceNoMember,2)},\t Tax-Exempt'


class Inventory:
    def __init__(self):
        self.inventory={}
        self.transactions=0
    def __str__(self):
        string=""

        for key in self.inventory: 
            string=string+self.inventory[key].__str__()+"\n"
        return string  
    def listProducts(self):
        string=""
        count=1
        for key in self.inventory: 
            string+=str(count)+".- "+key+"\n"
            count+=1
        return string  
    def addProduct(self,product):
        self.inventory[product.prodName]=product

    def upDate(self,Name,quantity):
        try:
            self.inventory[Name].quantity-=quantity
            if self.inventory[Name].quantity<=0:
                print("nooo",self.inventory[Name].quantity-quantity)
                # self.inventory.pop(Name)
# aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
            return True
        except:
            return False

class Cart():
    def __init__(self):
        self.items={}
        self.receipt=[]
    def __str__(self):  
        string=""
        for key in self.items: 
            string+=key+": "+str(self.items[key])+"\n"
        return string  
    def addItem(self,product,quantity):
        self.items[product]=quantity
    def removeItem(self,product,quantity):
        self.items.pop(product)
    def popItem(self,product,quantity):
        self.items.pop(product)
    def checkOut(self,store,member,cash):
        priceNoMember=0
        priceMember=0
        tax=0
        saves=0
        totalItems=0
        tempMemberValue=0
        tempNoMemberValue=0
        today=datetime.today()
        monthName=calendar.month_name[today.month]
        date=(monthName+" "+str(today.day)+","+str(today.year)+"\n" )
        TRANSACTION=str(3)
        text=[date,"TRANSACTION:"+TRANSACTION.zfill(6)+"\n","ITEM\t\tQUANTITY\t\tUNIT PRICE\tTOTAL\n"]
        nextItem=""
        if member:
            for i in self.items:
                nextItem=i
                totalItems+=self.items[i]
                tempMemberValue=store.inventory[i].priceMember*self.items[i]
                tempNoMemberValue=store.inventory[i].priceNoMember*self.items[i]
                priceMember+= tempMemberValue  
                priceNoMember+= tempNoMemberValue
                tax+=round((store.inventory[i].taxStatus*0.065)*(tempMemberValue),2)
                while len(nextItem)<12:
                    nextItem+=" "
                text.append(nextItem+"\t\t"+str(self.items[i])+"\t\t"+"$"+str(store.inventory[i].priceMember)+"\t\t"+str(tempNoMemberValue)+"\n")
                # print(store.inventory[i].taxStatus, "taxXSTatus")

                store.upDate(i,self.items[i])

        else:
            for i in self.items:
                nextItem=i
                totalItems+=self.items[i]
                tempNoMemberValue=store.inventory[i].priceNoMember*self.items[i]
                priceNoMember+= tempNoMemberValue
                tax+=round((store.inventory[i].taxStatus*0.065)*(tempMemberValue),2)
                nextString=i+str(self.items[i])+"$"+str(store.inventory[i].priceMember)+str(tempNoMemberValue)
                while len(nextItem)<12:
                    nextItem+=" "
                text.append(nextItem+"\t\t"+str(self.items[i])+"\t\t"+"$"+str(store.inventory[i].priceMember)+"\t\t"+str(tempNoMemberValue)+"\n")
            priceMember=priceNoMember
        text.append("************************************************\n")
        text.append("TOTAL NUMBER OF ITEMS SOLD:"+str(totalItems)+  "\n")
        text.append("SUB-TOTAL: $"+     str(priceMember)+           "\n")
        text.append("TAX(6.5%): $"+     str(tax)+                   "\n")
        text.append("TOTAL:$"+          str(tax+priceMember)+       "\n")
        text.append("CASH:$"+           str(cash)+                  "\n")
        text.append("CHANGE:$"+         str(round(cash-(tax+priceMember),2))+         "\n")
        text.append("************************************************\n")
        text.append("YOU SAVED:$"+      str(round(saves,2))+       "!\n")
        saves=priceNoMember-priceMember
        return text
    def printReceipt(self,texto):
        """ Saves the created input in a txt file"""

        fout=open("receipt.txt", 'wt')
        for line in texto:
            fout.write(line )
        # fout.write('\n')
        fout.close 