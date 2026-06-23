# Example 1: Functions Without Parameters

def greet():
    print("Welcome to the python functions: ")

greet()

greet()

#Example 2: Function With Parameter

def add_numbers(a,b):
    result=a+b
    print("Sum is : ",result)

add_numbers(10,30)  

# Example 3: Function with Return value

def multiply(a,b):
    return a*b

result2=multiply(5,6)
print("Multiply is : ", result2)

# Example 4: Function with Input

def look():
    name = input("Enter your name: ")
    print("Welcome to the Function area: ", name)

look()
