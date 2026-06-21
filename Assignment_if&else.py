#1 First question
num = int(input("Enter your number :"))

if num>100:
    print("Big Number")
else:
    print("Small Number")

# Name and Age

name = input("What is your name :")
age = int(input("Enter your number :"))

if (age>=60):
    print("Senior Citizen")
else:
    print("Adult")
    

# Ask for two numbers

num1 = int(input("Enter your First Number"))
num2 = int(input("Enter your Second Number"))

if num1>num2:
   print("Larger number is:", num1)
else:
    print("Larger number is:", num2)

# Ask for password

password = input("Enter your password : ")

if password == "skill@123":
    print("Login Successfull")
else:
    print("Access Denied")