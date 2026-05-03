# --> *args ---> Extra positional arguments written inside a tuple type
#Example 1
def example(a, b, *args):
    print(a, b, args)
example(1, 2, 3, 4, 5)

#Example 2 (Basic behavior)
def demo(*args):
    print(args)
demo(1, 2, 3)

#Example 3 (Sum of numbers)
def sum_all(*numbers):
    total = sum(numbers)
    print(f"The sum of {numbers} is {total}")
sum_all(1, 2, 3, 4)  
sum_all(10, 20)      

#--> **kwargs --> Extra keyword arguments written inside a dict type
#Example 1 (Basic Example)
def demo(**kwargs):
    print(kwargs)
demo(a=1, b=2)

#Example 2 (Function calls)
data = {"name": "Alice", "age": 30}
print(**data)

#Example 3 (args and kwargs)
def greet(*names, greeting="Hello", **options):
    for name in names:
        msg = f"{greeting}, {name}"
        if options.get("uppercase"):
            msg = msg.upper()
        print(msg)
greet("Alice", "Bob", greeting="Hi", uppercase=True)
