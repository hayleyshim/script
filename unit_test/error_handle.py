first = int(input("first number please: "))
second = int(input("second number please: "))

try:
    result = first + second
    print("the result for sum is :", result)
except:
    print("exception part!")

try:
    result = first / second
    print("the result for devision is : ", result)
except:
    print("devide by zero is not allowed!")
