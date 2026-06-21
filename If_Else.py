#1. Eligible for vote


age =int(input("Enter your age:"))

if (age>=18):                               #IF statement
    print("You are eligible for vote.")     #True-Output
else:                                       #Else Statement
    print("You are not eligible for vote.") #Falst - Output 


#Real Example : -   Checking for Even or ODD

num=int(input("Enter a number:"))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")



#Eg. Pass or Fail

marks=int(input("Enter your marks : "))

if marks>=35:
    print("Passed")
else:
    print("Failed")

    

#3. Traffic Lights

light =  input("What is the signal color :")
if light == "red":
    print("stop")

else:
    print("Wait")
