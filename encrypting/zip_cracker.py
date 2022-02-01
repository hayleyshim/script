from zipfile import Zipfile
from datetime import datetime

zf = input("please give me the zipfile: ")
passlist = input("please give me the passlist: ")

zf = zipfile(zf)
test = 0
start_time = datetime.now()
for password in open(passlist):
    password = password.strip("\n")
    print("tested: {}".format(password))
    test += 1
    try:
        zf.extractall(pwd=password.encode())
        end_time = datetime.now()
        t = start_time - end_time
        print("_"*50)
        print("password found: {} || {} password tested in {} seconds !".format(password, test, t.total_seconds()))
        break
    except:
        continue