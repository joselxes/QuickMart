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
        string=[]
        count=1
        for key in self.inventory: 
            string.append(key)
            count+=1
        return string  
    def addProduct(self,product):
        self.inventory[product.prodName]=product

    def increaseTransactions(self):
        self.transactions+=1
        
    def upDate(self,Name,quantity):
        try:
            if self.inventory[Name].quantity<quantity:
                self.inventory[Name].quantity=0
            else:
                self.inventory[Name].quantity-=quantity
            return True
        except:
            return False

class Cart():
    def __init__(self):
        self.items={}
        self.subTotal=0
        self.tax=000
        self.total=0
        self.change=0
        self.saved=0
        self.receipt=[]

    def __str__(self):  
        string=""
        count=1
        if len(self.items)==0:
            return "\n---The cart is empty---\n"
        for key in self.items: 
            string+=str(count)+".- "+key+": "+str(self.items[key])+"\n"
            count+=1
        return string  
    def listItems(self):  
        string=[]
        for key in self.items: 
            string.append(key)
        return string  
    def addItem(self,product,quantity):
        if product in self.items:
            self.items[product]+=quantity
        else:
            self.items[product]=quantity

    def removeItem(self,product,quantity):
        self.items[product]-=quantity
        if self.items[product]<=0:
            self.items.pop(product)

    def empty(self):
        if len(self.items)>=1:
            return False
        return True
    def checkOut(self,store,member,cash,onlyView):
        priceNoMember=0
        priceMember=0
        totalItems=0
        tempMemberValue=0
        tempNoMemberValue=0
        today=datetime.today()
        monthName=calendar.month_name[today.month]
        date=(monthName+" "+str(today.day)+","+str(today.year)+"\n" )
        if not(onlyView):
            store.increaseTransactions()
        receiptName= "transaction_"+str(store.transactions).zfill(6)+"_" + str(today.month) + str(today.day) + str(today.year)  +"_"+".txt"
        receiptText=[date,"TRANSACTION:"+str(store.transactions).zfill(6),"ITEM\t\tQUANTITY\t\tUNIT PRICE\tTOTAL\n"]
        nextItem=""
        if member:
            for i in self.items:
                nextItem=i
                totalItems+=self.items[i]
                tempMemberValue=store.inventory[i].priceMember*self.items[i]
                tempNoMemberValue=store.inventory[i].priceNoMember*self.items[i]
                priceMember+= tempMemberValue  
                priceNoMember+= tempNoMemberValue
                self.tax+=round((store.inventory[i].taxStatus*0.065)*(tempMemberValue),2)
                while len(nextItem)<12:
                    nextItem+=" "
                receiptText.append(nextItem+"\t\t"+str(self.items[i])+"\t\t"+"$"+str(store.inventory[i].priceMember)+"\t\t"+str(tempNoMemberValue)+"\n")
                # print(store.inventory[i].taxStatus, "taxXSTatus")
                if not(onlyView):
                    store.upDate(i,self.items[i])

        else:
            for i in self.items:
                nextItem=i
                totalItems+=self.items[i]
                tempNoMemberValue=store.inventory[i].priceNoMember*self.items[i]
                priceNoMember+= tempNoMemberValue
                self.tax+=round((store.inventory[i].taxStatus*0.065)*(tempNoMemberValue),2)
                nextString=i+str(self.items[i])+"$"+str(store.inventory[i].priceNoMember)+str(tempNoMemberValue)
                while len(nextItem)<12:
                    nextItem+=" "
                receiptText.append(nextItem+"\t\t"+str(self.items[i])+"\t\t"+"$"+str(store.inventory[i].priceMember)+"\t\t"+str(tempNoMemberValue)+"\n")
                if not(onlyView):
                    store.upDate(i,self.items[i])
            priceMember=priceNoMember
        self.subTotal=priceMember
        self.saved=priceNoMember-priceMember
        self.total=round(self.tax+priceMember,2)
        receiptText.append("************************************************")
        receiptText.append("TOTAL NUMBER OF ITEMS SOLD:"+str(totalItems) )
        receiptText.append("SUB-TOTAL: $"+     str(self.subTotal))
        receiptText.append("TAX(6.5%): $"+     str(self.tax))
        receiptText.append("TOTAL:$"+          str(self.total))
        receiptText.append("CASH:$"+           str(cash))
        receiptText.append("CHANGE:$"+         str(round(cash-(self.total),2)))
        receiptText.append("************************************************")
        receiptText.append("YOU SAVED:$"+      str(round(self.saved,3))+ "!")

        return receiptName,receiptText
    def printReceipt(self,receiptName,receiptText):
        """ Saves the created input in a txt file"""

        fout=open(receiptName, 'wt')
        for line in receiptText:
            fout.write(line+"\n")
        # fout.write('\n')
        fout.close 