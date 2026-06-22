# password validation 

# Counters for result tracking

valid_count = 0
invalid_count = 0

# Loop to take 5 password inputs

for i in range(1, 6):
    password = input(f"Enter password {i}: ")
    
    # Check if password contains at least one digit
    has_digit = any(char.isdigit() for char in password)

    # Apply all 3 conditions
    if len(password) >= 8 and "@" in password and has_digit:
        print(f"'{password}' is VALID \n")
        valid_count += 1
    else:
        print(f"'{password}' is NOT valid \n")
        invalid_count +=1

# Final summary
print("------ Summary ------")
print("Valid passwords  :", valid_count)
print("Invalid passwords:", invalid_count)
