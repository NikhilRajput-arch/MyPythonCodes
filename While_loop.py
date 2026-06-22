# Count from 1 to 5
i= 1
while i<=10:
    print(i)
    i = i+1  #incement to avoid infinite loop

# Password Retry system
password=""

while password!="admin@123":
    password = input("Enter Password:")
    
print("Login Successful ✅")          #outside of loop once the condition false


# Recharge System
balance = 50

while balance>0:
    print("Using internet....Balance Left:", balance)
    balance -=5

print("Internet disconnected. Please Recharge")

    
