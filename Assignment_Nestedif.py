# question 1

user = input("Enter your username :")
if user == "admin":

    password = input("Enter your password :")
    if password == "admin123":
        print("Welcome, admin!")
        
    else:
        print("incorrect password")

else:
    print("invalid username")
    

    # Question 2 ( AGE + LICENSE CHECK)

  
age = int(input("Enter your age : "))
if age>=18:

        ask = input("Tell me if you have license : ")
        if ask == "yes":
            print("You can drive")

        else:
            print("Get your license first")

else:
        print("You are underage")
        

# 3  (Simple ATM Simulator)

pin = int(input("Enter your pin : "))
if pin == 1234:
      
      ask = int(input("Enter your withdrawl money : "))

      if ask>=10000:
            print("Transaction Succesfull")
      else:
            print("Limit Exceeded")

else:
      print("Wrong pin")
    

    



