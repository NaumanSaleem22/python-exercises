#########################################################################################################
# Exercise 1 : # Let's build a small employee information program.
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# monthlySalary = float(input("Please enter your monthly salary: "))
# annualSalary = monthlySalary * 12

# print("Hello",name, "with age of",age, "having an annual salary of",annualSalary)


#########################################################################################################
# Exercise 2 : calculator

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

print(f"Addition: {add}")
print(f"Subtraction: {subtract}")
print(f"Multiplication: {multiply}")

if num2 != 0:
    division = num1 / num2
    print(f"Division: {division}")
else:
    print("Error: Division by zero is not allowed")