mul_value = 0
def mul_number(num1, num2):
    mul_value = num1 * num2
    print("local value: ", mul_value)
    return mul_value
mul_number(12,2)
print("global value: ", mul_value)
