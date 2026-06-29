# List Comprehension

#9.1 Transform items 

nums = [1,2,3,4,5,6,7,8,9]

squares = [n*n for n in nums]

print(squares)

#9.2 Long Verion

squares2 = []

for n in nums:
    squares2.append(n*n)

print("square 2 : ", squares2)    

# Filter items with Condition - Even or Odd Numbers:

nums1 = [10,21,32,43,54]
evens = [n for n in nums1 if n%2 == 0]

print("Filtering Even : ", evens)

# With odd just remove 0 add 1

nums1 = [10,21,32,43,54]
odds = [n for n in nums1 if n%2 == 1]

print("Filtering Odds : ", odds)

# Long Version

even2 = []
for n in nums1:
    if n%2 == 0:
        print(n)
    even2.append(n) 

print('Evens2 : ', even2)   

#9.3 Print Even or Odd

nums3 = [11,35,67,86,37,48,92]
result = ["Even" if n%2 == 0 else "Odd" for n in nums3]

print(result)

# Nesting

Colors = ['Blue', 'white', 'red', 'yellow', 'Blue']
sizes = ['M', 'L', 'XL', 'XS']

combos = [c+ "-" +s for c in Colors for s in sizes]

print(combos)

# List Flatten 

matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]

print(flat)