import getpass

user_name = getpass.getpass("user_name: ")
print("please enter your username: ", user_name)
while True:
    passwd = getpass.getpass("enter the password: ")
    if passwd == "python":
        print("welcom!")
    else:
        print("the pass you entered is incorrect!")


"""password = getpass.getpass(prompt = "please enter your password: ")
if password == 'python':
    print('welcom!')
else:
    print('the password you entered is encorrect!')"""


"""try:
    p = getpass.getpass("please enter your password: ")
except Exception as error:
    print('ERROR', error)
else:
    print("password is: ", p)"""
