from parse import compile

p = compile("It's {}, I love it")
print(p)

result = p.parse("It's a beautiful day, I love it")

print(result)