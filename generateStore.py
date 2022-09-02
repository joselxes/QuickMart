from random import  randrange
import random

def main():
    minimoItems=0
    maximoItems=30
    taxExemptItems=["Butter",
    "Coffe",
    "Cocoa",
    "Crackers",
    "Eggs",
    "Fish",
    "Gelatins",
    "Honey",
    "Rice",
    "Noodle",]
    taxItems=["lotion",
    "makeup",
    "soap",
    "cups",
    "pints",
    "cream",
    "lenses",
    "perfume",
    "cream",
    "cologne",]
    store=[]

    for i in range(0,random.randint(5,10)):

        if random.randint(0,1):
            index=random.randint(0,len(taxExemptItems)-1)
            store.append(taxExemptItems[index])
            taxExemptItems.pop(index)
            store[i]+=": "+str(random.randint(minimoItems,maximoItems))
            price=random.randint(5,100)+random.randint(0,99)/100
            store[i]+=", $"+str(price)
            store[i]+=", $"+str(round(price+(price*0.05),2))
            store[i]+=(", Tax-Exempt")
        else:
            index=random.randint(0,len(taxItems)-1)
            store.append(taxItems[index])
            taxItems.pop(index)
            store[i]+=": "+str(random.randint(minimoItems,maximoItems))
            price=random.randint(5,100)+random.randint(0,99)/100
            store[i]+=", $"+str(price)
            store[i]+=", $"+str(round(price+(price*0.05),2))
            store[i]+=(", Taxable")
        
    fout=open("inventory.txt", 'wt')
    for line in store:
        fout.write(line+"\n")
    # fout.write('\n')
    fout.close 






if __name__ == "__main__":
    main()


