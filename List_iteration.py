# 8.1 Simple For Loop

subjects = ["maths", "science", "English"]
for subject in subjects:
    print(subject)

#8.2 Index using range

for i in range(len(subjects)):
    print(i, subjects[i])

#8.3 enumerate

for i, s in enumerate (subjects):
    print(i, s)

#8.4 While loop

i=0
while i>= len(subjects):
    print(i, subjects[i])
    i+=1

#8.5 Looping nested list

marks = [[45,67,87],[66,89,47],[77,67,84]]           # 3 Subjects for 3 students
for i, student_marks in enumerate (marks, start=1):
    Total=sum(student_marks)
    print("student :",i, "Marks :",marks[i-1], "total",Total)