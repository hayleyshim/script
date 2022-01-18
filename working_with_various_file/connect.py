import mysql.connector

print('connecting...')
con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='oms')
cursor = con.cursor()
print('connected!')
print('inserting...')
cursor.execute('INSERT INTO student VALUES(3,\'JM\',\'yh\', \'yhshim@gmail.com\', \'+1234\')')
con.commit()
print('inserted!')
con.close()
