''' 
CALCULATOR  

TASK 2

Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.

Perform the calculation and display the result.

CODSOFT
BATCH :- A63 (10th JULY - 10th AUGUST)
SUBMITTED BY :- ABHINAV PANDEY
'''
print("OPERATIONS TO BE PERFORMED ON NUMBERS....")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

op = int(input("SELECT OPTION TO PERFORM OPERATION: "))

if op == 1:
    print("ADDITION OF TWO NUMBERS BEGIN")
    num1 = float(input("ENTER FIRST NUMBER: "))
    num2 = float(input("ENTER SECOND NUMBER: "))
    result = num1 + num2
    print("THE RESULT IS:", result)
elif op == 2:
    print("SUBTRACTION OF TWO NUMBERS BEGIN")
    num1 = float(input("ENTER FIRST NUMBER: "))
    num2 = float(input("ENTER SECOND NUMBER: "))
    result = num1 - num2
    print("THE RESULT IS:", result)
elif op == 3:
    print("MULTIPLICATION OF TWO NUMBERS BEGIN")
    num1 = float(input("ENTER FIRST NUMBER: "))
    num2 = float(input("ENTER SECOND NUMBER: "))
    result = num1 * num2
    print("THE RESULT IS:", result)
elif op == 4:
    print("DIVISION OF TWO NUMBERS BEGIN")
    num1 = float(input("ENTER FIRST NUMBER: "))
    num2 = float(input("ENTER SECOND NUMBER: "))
    if num2 != 0:
        result = num1 / num2
        print("THE RESULT IS:", result)
    else:
        print("ERROR: Division by zero is not allowed.Check again num2.Check again!")
else:
    print("INVALID OPTION SELECTED! CHECK YOUR OPTION")
