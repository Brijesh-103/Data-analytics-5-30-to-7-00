# How to find area of circle (use only oprators) ?

```python
 pi = 3.14
 r = 5
 area = pi*(r**2)
 print(area)

```

# how to find area of rectangle

```python
l = 10
b = 5
area = l*b
print(area)
```

# how to find area of square

```python
s = 4
area = s**2
print(area)
```

# how to find area of triangle

```python
b = 10
h = 5
area = 0.5*b*h
print(area)
```

# w a p to print your full address.

```python
full_address = "Achivers pg,\nuniversity road,\nrajkot 360005"
print(full_address)
```

# w a p to swap two numbers using third variable and without using third variable

```python
# using third variable
a = 10
b = 20
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)

# without using third variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)
```


# w a p t check voting eligibility (Withoout using any conditional statement,, return true if eligible otherwise false)

```python
age = int(input("Enter your age: "))
is_eligible = age >= 18
print(is_eligible)
```

# 5. w a p t find student result system
* input:-  student name, marks of 3 subject
* calculate :- persentage of student, check student fail or pass when persentage grater then 40

```python
student_name = input("Enter student name: ")
marks_subject1 = float(input("Enter marks of subject 1: "))
marks_subject2 = float(input("Enter marks of subject 2: "))
marks_subject3 = float(input("Enter marks of subject 3: "))
total_marks = marks_subject1 + marks_subject2 + marks_subject3
percentage = (total_marks / 300) * 100
is_pass = percentage >= 40
print("Student Name: ", student_name)
print("Percentage: ", percentage, "%")
print("Pass: ", is_pass)
```

