# Example 1 : Bank loan Eligibility

age=int(input("Enter yoru age:"))


if age>=18:
    salary=int(input("Enter your Salary :"))
    if salary>=30000:
        print("You are eligible for loan.")
    else:
        print("Your salary is too low for loan.")
else:
    print("You must be at least 18 to apply for a loan.")


#2.Exam Grading system

marks=int(input("Enter your Marks :"))

if marks>=90:
    print("Grade : A++")
else:
    if marks>=75:
        print("Grade : A+")
    else:
        if marks>=60:
            print("Grade : A")
        else:
            if marks>=35:
                print("Grade : B")
            else:
                print("Fail")

                
