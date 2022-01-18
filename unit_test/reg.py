import re
txt = 'my name is syh and i am from korea'
#x = re.findall('N', txt)
#print(x)

x = re.search('syh',txt)
print(x)
if x == None:
    print("nothing found!")
else:
    print("something found!")

#print('the first white-space is located in position', x.start(), 'index')

x = re.split('\s', txt)
print(x)

x = re.sub('\s', '0', txt)
print(x)