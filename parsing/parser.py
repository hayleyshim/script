from parse import *

result = parse("It's {}, I love it", "It's a beautiful day, I love it")

result2 = parse("The {} who say {}", "The knights who say Ni!")

result3 = parse("Bring out the holy {item}", "Bring out the holy hand grenade")

result4 = parse("My quest is {quest[name]}", "My quest is to seek the holy grail!")

print(result)
print(result2)
print(result3)
print(result4)