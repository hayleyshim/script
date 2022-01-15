#username = input("Enter the username : ")
#print("the username is %s" %username)

import random

secret_no = random.randrange(1,10)
#print(secret_no)
count = 0
quess_limit = 10

while count < quess_limit:
    quess = int(input("please quess the number from 1- 10"))
    count += 1
    if quess == secret_no:
        print("wow you won the game!!")
        break

else:
    print("the correct number is %i" % secret_no)


