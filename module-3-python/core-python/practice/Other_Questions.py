# w a p to print your full address.
# full_address = "Achivers pg,\nuniversity road,\nrajkot 360005"
# print(full_address)

# w a p to swap two numbers using third variable and without using third variable
# using third variable
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print("Using 3rd veriable", "a =", a, "b =", b)


# without using third variable
# a = 10
# b = 20
# a = a + b
# b = a - b
# a = a - b
# print("Without using 3rd veriable", "a =", a, "b =", b)



# w a p t check voting eligibility

# age = int(input("Enter your age: "))
# is_eligible = age >= 18
# print(is_eligible)


# w a p t find student result system

# * input:-  student name,  marks of 3 subject
# * calculate :- %  of student, check student fail or pass when % <= 40

student_name = input("Enter student name: ")
marks_subject1 = float(input("Enter marks of Science: "))
marks_subject2 = float(input("Enter marks of English: "))
marks_subject3 = float(input("Enter marks of DA:"))
total_marks = marks_subject1 + marks_subject2 + marks_subject3
percentage = (total_marks / 300) * 100
is_pass = percentage >= 40
print("Student Name: ", student_name)
print("Percentage: ", percentage, "%")
print("Pass: ", is_pass)