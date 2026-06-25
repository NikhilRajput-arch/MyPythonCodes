# 5. Updating, Adding & Removing Items

# Change an item by index
fruits=["apple", "banana","cherry"]
#fruits[1]="mango"  #banana replaced
print(fruits)

# Add items
fruits.append("grapes")    #add at end
print(fruits)

fruits.insert(1, "orange")    #add at index 1
print(fruits)

more=["kiwi", "papaya"]        
fruits.extend(more)             # add another list
print(fruits)

# Remove items
fruits.remove("apple")  # removes first match
print(fruits)

last_item = fruits.pop()        # remove last, return it
print(fruits)
print("Popped Item: ",last_item)

at_item = fruits.pop(2)        # remove last, return it
print(fruits)
print("Popped Item: ",at_item)

fruits.clear()
print(fruits)