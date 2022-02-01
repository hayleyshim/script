from hashlib import sha1

hash = input('enter the hashed text: ')

passlist = open('passwordlist.txt')

for password in passlist:
    password = password.strip('\n')
    print('testing : {}'.format(password))
    hash_of_password = sha1(password.encode()).hexdigest()
    if hash_of_password == hash:
        print('*'*30)
        print('password found: {}'.format(password))
        break