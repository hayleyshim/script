class person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        person.count = person.count+1
    def get_name(self):
        print("name is %s " % self.name)
    def get_age(self):
        print("age is %i" % self.age)
    def birthday(self):
        self.age = self.age + 1
        print("happy birthday to %s" % self.name)
    def return_count(self):
        return(person.count)

sara = person("sara", 45)
sara.get_name()
sara.get_age()
sara.birthday()
sara.get_age()
sara.return_count()
print("now we have %i person present" % sara.return_count())
yh = person("syh", 32)
yh.get_name()
print("now we have %i person present" % yh.return_count())

john = person("john", 80)
print("now we have %i person present" % yh.return_count())

#print(sara)



