#########################################################

# Exercise 1: Number printer
# for i in range(1,11): 
#     print(i)


########################################################$

#Exercise 2: Even numbers

# i = 0

# while i < 21:
#     if i % 2 == 0 :
#         print(i)

#     i += 1    


#########################################################

#Exercie 3: Multiplication task

# num = int(input("Please enter a number: "))
# i=0
# while i <=10:
#     print(f"{num} x {i} = {num*i}")
#     i+=1

# num = int(input("Please enter a number: "))
# i=0
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")
    


#########################################################

#Exercies 4: Login Attempts

# i=0
# is_logged_in = False
# while i < 3: 
#     username = input("Enter your username: ") 
#     password = input("Enter your password: ") 
#     if username!="admin" or password!="admin":
#         print("Try again")
#         print(f"You have {2-i} attempts left") 

#     elif username=="admin" and password=="admin":
#         print("Login Successful")
#         is_logged_in = True
#         break

#     i+=1

# if is_logged_in == False:
#     print("Account locked")


##########################################################

# Exercise 5: Active users

users = [
    {"name": "Ali", "active": True},
    {"name": "Ahmed", "active": False},
    {"name": "Sara", "active": True},
    {"name": "Usman", "active": True}
]

for user in users:
    if user["active"] == True:
        print(f"{user["name"]}")