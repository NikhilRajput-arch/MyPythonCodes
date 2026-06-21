#String Slicing & Method

name="Satish Dhawale"

print("Separate First Name :", name[0:6])  #'Satish' (from 0 to 5)
print("Separate Last Name :", name[7:])
print("Separate First Name :", name[:6])
print("Separate Last Name :", name[-7:])

#Reverse
print("Reverse Name :", name[::-1])

#String Methods

#1. Upper Case
text="python is easy"
#print(text.upper())
newtext=text.upper()
print("Uppercase:",newtext)

#2. Lowercase
text1="DATA SCIENCE"
print("lower case:", text1.lower())

#3. title() - Capitalizes the first letter of each word

msg ="welcome to python"
print("Message in Title:", msg.title())

#4. Strip() - Removes extra spaces from start & end
line="     Hello everyone     "
print("Output of Strip:", line.strip())

#5. Replace() - Replace text
msg2="Python is hard"
print("Replacing text :", msg2.replace("hard","easy"))

#6. Find() - show index position
line2="Learn Python Programming"
print("Finding: ", line2.find("Python"))

#7. Count -- count how many times word/ letter appears
fruit ="banana"
print("Couting:",fruit.count("a"))

#8. split() - splits string into list using seprators

data="name, age, location"
print("split list:", data.split(","))

#9. Join() - Joins list elements into one string
words=['Data','Science']
print("Joining: ", "".join(words))

#10. Startswith() and endswith()
course="Python Basics course"
print(course.startswith("Python"))
print(course.endswith("course"))