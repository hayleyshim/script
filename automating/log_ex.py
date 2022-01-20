import logging

logging.basicConfig(filename='log_ex.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x, y):
    return x * y
def divid(x, y):
    return x / y

num1 = 10
num2 = 8

add_result = add(num1, num2)
logging.debug('add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = substract(num1, num2)
logging.debug('sub: {} - {} = {}'.format(num1, num2, sub_result))

mul_result = multiply(num1, num2)
logging.debug('mul: {} * {} = {}'.format(num1, num2, mul_result))

divid_result = divid(num1, num2)
logging.debug('divid: {} / {} = {}'.format(num1, num2, divid_result))
