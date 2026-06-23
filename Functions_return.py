# Chain Return Value

def add(a,b):
    return a+b

def multiply(x):
    return x*3

# Use return value together

result = multiply(add(5,6))     #multiply(11)
print("Total : ", result)

# Version using only print statements

def add(a,b):
    print("Sum is : ", a+b)

def multiply(x):
    print("Multiplication is : ", x*2)

# Using Function statements Separately

add(5,4)                  # This is prints of sum does not store it
multiply(9)              # Manually using the value returned from add