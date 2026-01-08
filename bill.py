#Write a python program to print a SuperBill Market
from datetime import datetime

name=input("Enter your name:")

lists='''
Daawat Rice            RS 20/kg
Sugar                  Rs 30/kg
Salt                   RS 20/kg
Oil                    RS 90/liter
Maggi                  RS 20/kg
Panner                 RS 300/kg
Boost                  RS 90/each
Colgate                Rs 80/each
ChickenMasala          Rs 10/each
Dal                    RS 50/kg
Tamrid                 Rs 150/kg
'''
#Declaration
price=0
pricelist=[]
totalprice=0
FinalfinalPrice=0
ilist=[]
qlist=[]
plist=[]

#Rates for items
items={'Daawat Rice':20,
       'Sugar':30,
       'Salt':20,
       'Oil':90,
       'Maggi':20,
       'Panner':300,
       'Boost':90,
       'Colgate':80,
       'ChickenMasala':10,
       'Dal':50,
       'Tamrid':150}

option=int(input("for list of items press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is Not available.")
    else:
         print("You entered wrong number.")
    inp=input("Can I bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Vinay SuperMarket",25*'=')
            print(25*'','Konda')
            print("Name:",name,30*"","Date:",datetime.now())
            print("sno",8*"",'items',8*"",'Quantity',3*"",'price')
            for i in range(len(pricelist)):
                print(i,8*'',8*'',ilist[i],6*'',qlist[i],9*'',plist[i])
            print(75*"-")
            print(48*"",'TotalAmount:',"RS",totalprice)
            print("gst amount",50*"","RS",gst)
            print(75*"-")
            print(48*"",'finalAmount:',"RS",finalamount)
            print(75*"-")
            print("Thanks for visiting!")


