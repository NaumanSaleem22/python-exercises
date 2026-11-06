############################################################

# Exercise 1 — Basic Function

# def welcome():
#     print("Welcome to FDE Learning!")

# welcome()


###########################################################

# Exercise 2 — Calculator Function

# def calculate_total(price, quantity):

#     result = price * quantity

#     return result

# print(calculate_total(7000, 3))


############################################################

# Exercise 3 — Salary Calculator

# def calculate_salary(monthly_salary, bonus=0):

#     annual_salary = monthly_salary * 12
#     final_salary = annual_salary + bonus
#     return final_salary

# print(calculate_salary(70000, 10000))
# print(calculate_salary(30000))
 

################################################################

# Exercise 4 — User Access System

# def check_acces(username, password ,role, is_active):
#     if username == "admin" and password == "12345" and role =="admin" and is_active:
#         return "Access Granted"
#     else:
#         return "Access Denied"

# print(check_acces("admin", "12345", "admin", True))
# print(check_acces("Nouman", "3233 ","admin", False))


# Exercise 5 - Calculate Discount

def calculate_discount(price, discount_percentage):

    discount_amount = price * discount_percentage / 100
    final_price = price - discount_amount

    return final_price

print(calculate_discount(10000, 20))