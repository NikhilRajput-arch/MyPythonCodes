#1. Multiplication Table

for i in range(1,6):        #Outer Loop for each number
    for j in range(1,11):   #Inner Loop for Multiplication
        print(i, "x", j, "=", i*j)
    print("-"*15)


# 2. Star Pattern

for row in range(1,6):
    for col in range(1, row+1):
        print("*", end=" ")
    print()


