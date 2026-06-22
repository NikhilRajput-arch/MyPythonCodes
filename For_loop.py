# Print numbers 1 to 8
for i in range(1, 8):
    print(i)

# Print your name 4 times
for i in range(4):
    print("Nikhil Rajput")

# Print odd numbers between 1 and 20
for i in range (1, 21, 2):
    print(i)

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print("Fruit Name: ",f)

# Looping through a string
name = "Nikhil"
for char in name:
    print("My Name : ",char)

# Practical Use
employees = ["Nikhil", "Rohit", "Amit", "Suresh"]
for emp in employees:
    print(emp, "is a valuable employee of our company.")

# Password Validator
passwords = ["skill@123", "pass12", "hello@world","abc@12"]
for pwd in passwords:
    if len(pwd) >= 8 and "@" in pwd:
        print(pwd, "is a valid password.")
    else:
        print(pwd, "is an invalid password)")
