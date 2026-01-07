#list methods
students=['Ram','Ravi','Vinay','Sweety','Sunny']
print(students.count("Ravi"))
print(students.index("Sunny"))
students.insert(5,"Arjun")
print(students)
students.reverse()
print(students)
print(len(students))
students.sort()
print(students)

students.sort(reverse=True)
print(students)
a=students
print(id(students))
print(id(a))
print(a==students)

b= students.copy()
print(b)
students.insert(0,"bunny")
print(students)
students.remove("Ravi")
print(students)
print(students.pop(0))
students.clear()
print(students)
print()

#Travarsing of lists
age=[12,14,18,24]
for index in range(len(age)):
    print(f"indexValue of'{age[index]}'is {index}")
print()

#Nested lists-->A list inside another list
asia=[['India','paris','Kashmir'],['Korea','UK','US'],['bihar','china','japan']]
print(asia)
asia[0][1]="Patna"
print(asia[0][1])
print(asia[0])
print(asia[2][1])

print()

#print list elements through user
list_items=[]
total_items=int(input("Enter the number of elements:"))
for i in range(total_items):
    item=input("Enter the list item:")
    list_items.append(item)
    print(f"List items are {list_items}")
print()

#Delete list element in list by using remove(),pop(),delete(),clear()
#del()-->used to delete a value through index and slice
a=[1,2,3,6,7,9,5]
del a[2:4]
print(a)
del a[3]
print(a)
print()

#pop()-->used to pop a value by using index value
a=[1,2,3,6,7,9,5]
a.pop(3)
print(a)
print()

#remove() used to remove a value from list 
a=[4,8,24,14,5,2,3,6]
a.remove(14)
print(a)

#List Comprehesion--> to minimize the code lines
str1=[1,6,6,6,6,6,6,6,6,6,2,3,5,5,6]
n=[]
for i in str1:
    if i==5:
        str1.remove(5)#to use  remove() delete only one value
    else:
            n.append(i)
            print(n)
print()

#find a repeated values through index
s=[1,2,3,4,6,7,3,7,8,9]
for i in range(len(s)):
  if s[i]==3:
    print(i)#to delete repeated value at a time and print their index
print()


list=["Even" if i%2==0 else 'odd' for i in range(10)]
print(list)
print()

fruits=["Apple","Mango","orange","Grapes","Banana"]
newlist=[x for x in fruits if "l" in x]
print(newlist)
print()


#program to check if lists contain the same elements regardless of the order
def check_contest(nums1,nums2):
 for x in set(nums1+nums2): 
  if nums1.count(x)!=nums2.count(x):
     return False 
 return True
nums1=[1,2,3]
nums2=[3,2,1]
print("Original list elements are:")
print(nums1)
print(nums2)
print(check_contest(nums1,nums2))
nums1=[1,2,3]
nums2=[1,2,3]
print("Original list elements are:")
print(nums1)
print(nums2)
print(check_contest(nums1,nums2))
nums1=[1,2,3]
nums2=[4,2,1]
print("Original list elements are:")
print(nums1)
print(nums2)
print(check_contest(nums1,nums2))

print()
#Optimisation solution of the above program
def check_contest(nums1,nums2):
     return sorted(nums1)==sorted(nums2)
nums1=[1,2,3]
nums2=[1,2,3]
print(check_contest(nums1,nums2))
nums1=[1,2,3]
nums2=[4,2,1]
print(check_contest(nums1,nums2))
nums1=[1,2,3]
nums2=[3,2,1]
print(check_contest(nums1,nums2))
print()
#program to check if all the elements of a list are included in another given list
def test_includes_all(nums,list):
 for x in list:
     if x not in nums:
         return False
     return True 
print(test_includes_all([10,20,30,40,40,60],[20,30]))
print(test_includes_all([10,50,30,40,40,80],[20,40]))
print()

#write a python program to get cumulative sum of the elements of the given list
def cumulative_sum(nums):
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result
numbers = [1, 2, 3, 4, 5]
print("Cumulative sum:", cumulative_sum(numbers))
print()

#above program using itertools import accumalate
from itertools import accumulate

numbers = [1, 2, 3, 4, 5]
print(list(accumulate(numbers)))
