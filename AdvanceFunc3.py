'''*args allows a function to accept any number of positional arguments
Arguments are stored as a tuple
args is just a name (you can use anything), but * is mandatory.
'''
#Example1
def add(*args):
    return sum(args)
print(add(10, 20, 30))

#Example2 
#Basic args 
def show(*args):
    print(args)
    print(type(args))
show(10, 20, 30)

#Example 3
#Sum of number using *args
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(add(10, 20))
print(add(10, 20, 30, 40))

#Example 4
#Mixed Agrumnets
def display(name, *marks):
    print("Name:", name)
    print("Marks:", marks)
display("Amit", 80, 85, 90)

#Example 5
#Keyword Arguments
def show(**kwargs):
    print(kwargs)
    print(type(kwargs))
show(name="Ravi", age=20, city="Delhi")

#Example 6
#keyword arguments are arguments passed to a function using the parameter name, rather than relying only on position.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")
greet("Alice", 30)                
greet(name="Alice", age=30)       
greet(age=30, name="Alice")  

#Example 7
#Variable Keyword Arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
print_info(name="Alice", age=30, city="Paris")



