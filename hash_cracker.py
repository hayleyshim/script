from hashlib import sha1

hash = input("hashed please: ")
passlist = open("password.txt")
for password in passlist:
    password = password.strip("\n")
    print("testing: {}".format(password))
    hash_of_password = sha1(password.encode()).hexdigest()
    if hash_of_password == hash:
        print("_"*20)
        print("password : {}".format(password))
        break