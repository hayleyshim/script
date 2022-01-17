import re

txt = 'today is rain'
x = re.search('^today.*rainy$', txt)
if x:
    print('YES! We have one match!')
else:
    print('No Match!')