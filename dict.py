friends = {"name":"yh",
           "lastname":"shim",
           "dob":"1998"
}

x = friends["name"]
print(x)

for x in friends.values():
    print(x)

if "name" in friends:
    print("yes we have his name!")

friends["f/name"] = "john"
print(friends)

friends.pop("name")
print(friends)