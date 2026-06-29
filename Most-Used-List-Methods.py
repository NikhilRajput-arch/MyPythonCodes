# 6. Most-Used List Methods 

nums=[5,3,8,3]

#Append
nums.append(10)   #Adding 10 at the end
print(nums)

#insert
nums.insert(1, 99)  # add at certain position
print(nums)

# Extend
fruits=["apple","banna"]
more_fruits=["cherry","mango"]

fruits.extend(more_fruits)

print(fruits)


#Differnce Between append() and extend()

#Apeend
l1=[1,2]
l2=[3,4]
l1.append(l2)
print(l1)

#Extend
l3=[5,6]
l3.extend(l2)
print(l3)


# Finding Index of list items 
print(nums.index(8))


# Sorting Ascending
nums.sort()
print(nums)

# Sorting Descending
nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)

copy_nums=nums.copy() 
print(copy_nums)