''' 
Function is a block of code.
It runs only whe it is called.
It executes a specific task.
It helps to reduce a repetition of code.
'''
#Syntax:
def function_name():
    # block of code

#Example program 
def hello () :
  print ("Say Hello , World!")
hello()

#To add two numbers
def sum(a,b):
  print(a+b)
sum(10,20)

#function with retutrn value
def multiply(x, y):
    return x * y
result = multiply(5, 4)
print(result)

#check the number is even or odd
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(7))

#Factorial of a number:
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))

#Check given number is prime number or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))

#Default arguments
def default(name="Python"):
   print("Hello!",name)
default()  
