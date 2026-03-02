## LAB -01 

## PART 1 -- VARIABLES

## Student info
name = "wajiha"
age = 20
city = "Peshawar"

print(name)
print(age)
print(city)

## Two number operations
num1 = 10
num2 = 5

print("Sum:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)


## PART 2 – INPUT AND OUTPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name + ", you are", age, "years old")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)


## PART 3 -- COMMENTS
# This program shows basic Python concepts
# Like variables, input, arithmetic
# And loops

"""
Multi-line comment:
The program also asks user input
Performs arithmetic and conditions
"""



## PART 4 --- TYPE CHECK
a = 10
b = 3.14
c = "Hello"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))




## PART 5 --> DATA TYPE
age = int(input("Enter your age: "))
print("After 10 years, you will be:", age + 10)
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
average = (marks1 + marks2 + marks3) / 3
print("Average marks:", average)



## PART 6 -- CONDITIONS

## Task 1 -- Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

## Task 2 – Grade System
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

## Task 3 – Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("Not eligible")

## Task 4 – Print numbers 1 to 10
for i in range(1, 11):
    print(i)

## Task 5 – Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

## Task 6 – Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 numbers:", total)

## Task 7 –> Password Check
password = ""
while password != "admin1234":
    password = input("Enter password: ")
print("Correct password entered")

## Task 8 – Function average
def average(a, b, c):
    return (a + b + c) / 3

print("Average is:", average(10, 20, 30))

