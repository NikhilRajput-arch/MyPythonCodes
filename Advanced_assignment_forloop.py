# Loop from 1 to 5

for i in range(1, 6): # Loop from 1 to 5
    # The spaces before the lines below are CRITICAL
    password = input(f"Enter password {i}: ")
    
    if len(password) >= 8 and "@" in password:
        print(f"'{password}' is VALID\n")
    else:
        print(f"'{password}' is NOT valid\n")