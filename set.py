animals = {"fox", "cat", "dog"}
print(animals)

for x in animals:
    print(x)

print("foxs" in animals)
animals.update(["fox","bird"])
print(animals)
print(len(animals))

animals.remove("fox")
print(animals)

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)
