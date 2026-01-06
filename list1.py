kiran=[]
print(type(kiran))
print(kiran)
print()

#creation of list with various types of data
kiran=[1,2.2,"listExample"]
print(kiran)
print(type(kiran))
print()

#Accessing list by using positive and negative index number 
Fruits=['mango','apple','banana']
print(Fruits[1])
print(Fruits[-1])
print()

#Slicing of lists 
Animals=["Dog","Cat","Cow","Lion","Tiger"]
print(Animals[0:4:2])
print(Animals[0:2])
print(Animals[:2])
print(Animals[0:])
print(Animals[4:0:-2])
print(Animals[-4:2])
print(Animals[-3:4:1])
print(Animals[0:3+1])
print(Animals[0:4:-2])
print(Animals[-1])
print(Animals[-1:4:-2])
print(Animals[4:-2])
print(Animals[4:0])
print(Animals[::])
print(Animals[:])
print(Animals[::-1])
print(Animals[2:1])
print(Animals[4:-2])
print()


#Adding of two lists
list_1=[1,2,3]
list_2=[4,5,6]
print(list_1 + list_2)
print()

#multiply list
a=[5,2.2]
print(a*3)
print()

#Check given element present in list or not
a=["Pooji","vinay",1,2.3]
print (1 in a)
print(5 in a)
print()

#built in functions in list
num=[10,20,30,40]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print()

#any() and all() returns either true or false but list contain 0's all() shows false,any() always returns true only
print(any([1,2,0,0,3,0]))
print(all([1,2,3,4,5]))
print()
