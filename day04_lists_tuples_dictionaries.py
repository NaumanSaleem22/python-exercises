########################################################

# Exercise 1 — List operations

# users = ["Nouman", "Ali", "Pappu" , "Wamiq", "Bablu"]

# users.append("Salman")
# users.insert(3, "Hassan")
# users.remove("Pappu")

# print(users)


#########################################################

#Exercise 2 — Tuple

# cities = ("Karachi", "Lahore", "Paris" , "Berlin", "Lisbon")

# print(f"{cities[0]} , {cities[2]}, {cities[4]}")
 

###########################################################

# Exercise 3 — User dictionary

# user = {
#     "name" :"Nouman",
#     "email" : "nouman@email.com",
#     "age" :27,
#     "role" :"admin",
#     "phone" : 33444432,
#     "active" :True,
# } 

# print(user.get("email"))
# user["age"] = 28

##########################################################

# Exercise 4 — API response processing

# users = [
#     {"name": "Ali", "role": "admin", "active": True},
#     {"name": "Ahmed", "role": "customer", "active": True},
#     {"name": "Sara", "role": "admin", "active": False},
#     {"name": "Usman", "role": "admin", "active": True},
#     {"name": "Hamza", "role": "customer", "active": False}
# ]

# for user in users:
#     if user["active"] and user["role"] == "admin":
#         print(user["name"])


import json

user = {
    "name": "Nouman",
    "age": 27,
    "active": True
}

json_data = json.dumps(user)

python_data = json.loads(json_data)


print(json_data)
print(python_data)