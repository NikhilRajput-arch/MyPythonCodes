# 7. Built-in Functions that work on lists

nums = [10,20,5,40]
print(len(nums))    #No. of items count
print(max(nums))    #Max item 
print(min(nums))    #Min item
print(sum(nums))    #Addition
print(sorted(nums))   # Does not change is orignal 


# Convert other type sof list
word ="python"
chars=list(word)
print(chars)

# Enumerate  - assign index to items


# Without Enumerate
fruits=["apple", "banana", "mango"]

index=1
for fruit in fruits:
    print(index, fruit)
    index +=1

# With Enumerate

print("Output using Enum : ")
fruits1=["apple", "banana", "mango"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)