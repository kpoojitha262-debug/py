#Creation of Tuple
t1 = (10, 20, 30)
t2 = ("apple", "banana", "apple")
t3 = (1,)         
t4 = ()           
print(t1)
print(t2)
print(t3)
print(t4)

#Access tuples
t = (10, 20, 30, 40)
print(t[0])    
print(t[-1])   
print(t[1:3]) 

#Tuple Methods
t = (10, 20, 30, 20, 40, 20)
print("Tuple:", t)
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

#Tuple operations
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Tuple 1:", t1)
print("Tuple 2:", t2)
t3 = t1 + t2
print("\nConcatenation:", t3)
t4 = t1 * 3
print("Repetition:", t4)
print("\nIs 2 in t1?", 2 in t1)
print("Is 10 not in t1?", 10 not in t1)
print("\nLength of t1:", len(t1))
print("\nElements of t2:")
for i in t2:
    print(i)
print("\nFirst element of t1:", t1[0])
print("Last element of t2:", t2[-1])
print("Slice of t3 (2 to 5):", t3[2:5])
print("\nMinimum:", min(t3))
print("Maximum:", max(t3))
a, b, c = t1
print("\nUnpacked values:", a, b, c)
