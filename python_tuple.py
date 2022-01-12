tup1 = (1,2,3,4)

#print(tuple[-4:-2])

tuple1 = list(tup1)
tuple1[2] = "test"
tup1 = tuple(tuple1)
print(tup1)

for x in tup1:
    print(x)

if 1 in tup1:
    print("one is here")

print(len(tup1))

animals = ("fox","cat", "dog")
#print(type(animals))
#del animals
print(animals)

animals = ("fox", "cat", "dog")
numbers = (1,2,3,4,5,6)
tuple2 = animals + numbers
print(tuple2)