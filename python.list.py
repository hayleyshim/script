animals = ['dog', 'cat', 'parrot', 'fox']
print(animals[-5:-1])
animals[0]= "good animals"
print(animals)

for x in animals:
    print(x)

if "dog" in animals:
    print("dog exists")

#del animals
#animals.clear()
#print(animals)

list = ['a', 'b']
list2 = [1,2,3]
list3 = list + list2
print(list3)