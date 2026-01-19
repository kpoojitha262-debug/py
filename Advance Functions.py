#Functions with *args (Variable Length Arguments)
#Example program
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(10, 20, 30, 40))

#Functions with **kwargs (Keyword Arguments)
#It is used for named arguments.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_info(name="Josthna", branch="CSE", year=3)

#Nested functions : function inside another function
def outer():
    def inner():
        print("Inner function")
    inner()
outer()

#Returning Multiple Values
def calculate(a, b):
    return a+b, a-b, a*b
add, sub, mul = calculate(10, 5)
print(add, sub, mul)

