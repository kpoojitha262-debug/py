''' A lambda function is:
Anonymous (no name)
One-line function
Written using lambda keyword.'''
#syntax
lambda arguments : expression

# Examples
#Check even or odd
even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(even_odd(15))

# maximum of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(12, 7))

#Add two numbers
add = lambda a, b: a + b
print(add(10, 20))

#Square and CUbe of the number
square = lambda x: x * x
print(square(6))

cube = lambda x: x * x * x
print(cube(6))


# Lambda with map() : applies a function to each element of an iterable (like list, tuple) and returns a new iterator with the transformed values.
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

#example 2 : convert list of strings to uppercase
names = ["python", "java", "c"]
result = list(map(lambda x: x.upper(), names))
print(result)

#lambda with filter() : It selects elements from an iterable for which a condition is True.
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#Example2: Filter the numbers greater than 10
numbers = [5, 12, 8, 20, 3]
result = list(filter(lambda x: x > 10, numbers))
print(result)

#lambda with reduce() : Repeatedly applies a function to the elements of an iterable and returns a single cumulative value.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)

#Example 2 : Find maximum number in a list
from functools import reduce
numbers = [10, 25, 5, 30]
result = reduce(lambda a, b: a if a > b else b, numbers)
print(result)

