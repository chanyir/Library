users = [
    {"name": "Ron", "age": 30},
    {"name": "Dana", "age": 50},
    {"name": "Ronit", "age": 60},

]

# Print all ages
# Option 1
for i in range(len(users)):
    print(users[i]["age"])
print("---------------")
# Option 2 (for each)
for user in users:
    print(user["age"])