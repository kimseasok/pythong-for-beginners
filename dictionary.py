customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# access value in dictionary

print(customer["name"])

# safe access the value

print(customer.get("name"))

# add key to dictionary

customer["birthday"] = "Jan 01 1985"
