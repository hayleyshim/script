"""f = open('file.txt', 'a')
f.write('   hello this is for test only to the file.txt')
f.close()

q = open('file.txt', 'r')
print(q.read())
"""

"""f = open('new.txt', 'w')
f.write('hello some new text inside you!!')
f.close()

l = open('new.txt', 'r')
print(l.read())"""

import os

if os.path.exists('new.txt'):
    os.remove('new.txt')
else:
    print('the file is now here budy!!')