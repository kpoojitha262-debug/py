#creation of dictionary with mixed datatypes
mydic={"name":12}
print(mydic)
person={"name":"Vinay","age":19,"city":"pdp"}
print(person)
num={1:"pooji",2:"sunny"}
print(num)
mixdict={"fruits":"Apple",1:[2,4,5]}
print(mixdict)
floatdict={1:2.3,3:4,"Apple":"Red"}
print(floatdict)

#Access values by using key
person={"name":"Vinay","age":19,"city":"pdp"}
print(person)
print("Name:",person["name"])
print("Age:",person["age"])
print("City:",person["city"])
print()


#Assigning elements to dictionary
dict={}
dict[1]="Hi"
dict["Fruits"]="Apple"
print("Dict elements:",dict)
print()

person={"name":"Vinay","age":19,"city":"pdp"}
print(person)
person["occupation"]="Btech"
print(person)
print()
# Dictionary Methods
dict={1:2.3,3:4,"Apple":"Red","Dog":"Animal"}
cost=30
dict2=dict.fromkeys(dict,30)
print(dict2)
print(dict.items())
#or
person={"name":"Vinay","age":19,"city":"pdp"}
for a,b in person.items():
      print(a,b)
print(dict.keys())#Displays items
#or
person={"name":"Vinay","age":19,"city":"pdp"}
for a in person:
 print(a)#display keys only
print(dict.values())
del dict[1]
print(dict)
dict1=dict.copy()
print(dict1)
dict.pop(3)
print(dict)
dict.popitem()
print(dict)
value=dict.get(3)
print(dict)
dict.clear()
print(dict)
dict.update(dict2)
print(dict)
print()

#Dictionary Comprehension
cube={x:x*x*x for x in range(10)}
print(cube)

even_cubes={x:x*x*x for x in range(11) if x%2==0}
print(even_cubes)
print()
#Nested Dictionary
Ram={
    1:"Hi",
    2:"Hello",
    3:{1:"Welcome!"}
    }
print(Ram)
print(Ram[3][1])
print(Ram[3])
print()

                                                                                      #TUPLES
'''
tuple is immutable once it created it cannot be changeable
used to store a multiple items in a single variable,denoted in paranthesis and separated by commas
used in real time -->used to store a latititude and longitude our home store the coordinates of other locations
tuples are faster than lists
tuples make the code safe from any accidental modificaions(unchangeble)
'''
#creation of tuple
mohan=(1,2,3,4.5,"string")
print(type(mohan))
print(mohan[4])
print()
   # mohan[2]=5.7
   # print(mohan)#cannot assign values 
#tuple Operations
mohan=(1,2,3,4.5,8.9)
print(sum(mohan))
print(max(mohan))
print(min(mohan))
print(len(mohan))
print()

#convert tuple to list
vinay=(1,4,3,2,5,6,7,8.9)
print(vinay)
print(list[vinay])
print(list(vinay))
print()

#contatenate two tuples
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
print()

t1=(1,2,3)
t2=(4,5,6)
print(t1*3)
print()

#zip the tuples
t1=(1,2,3)
t2=(4,5,6)
s=zip(t1,t2)
print(tuple(s))
print()
#add two tuples
t1=(1,2,3)
t2=(4,5,6)
new=[]
for i,j in zip(t1,t2):
     new.append(i*j)
print(tuple(new))
print()
#mutilpy to tuples
t1=(1,2,3)
t2=(4,5,6)
new=[]
for i,j in zip(t1,t2):
     new.append(i+j)
print(tuple(new))
print()

#subtract tuples
t1=(1,2,3)
t2=(4,5,6)
new=[]
for i,j in zip(t1,t2):
     new.append(j-i)
print(tuple(new))
print()

#Atm program
user_name="Vinay"
pass_word="vinay@123"
username=input("Enter user name:")
password=input("Enter password:")
s='''
1.Credit
2.Debit
3.Mini Statement
4.Exit
'''
Amount=10000
if username==user_name and password==pass_word:
    while True:
        print(s)
        option=int(input("Select the option:"))
        if option==1:
            Credit_amount=float(input("Enter the Amount:"))
            print(f"After credit {Credit_amount}:",Amount+Credit_amount)
        elif option == 2:
                Debit_amount=float(input("Enter the amount:"))
                print(f"After credit {Debit_amount}:",Amount-Debit_amount)
        elif option==3:
                    print("Amount:",Amount)
        elif option==4:
            print("Exit")
        break
else:
    print("Incorrect")
    print("Try again!")



