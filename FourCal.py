class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first /self.second

a = FourCal(4,2)
FourCal.setdata(a, 4, 2)
a.setdata(4,2)
print(a.first)
print(a.second)

a = MoreFourCal(4,2)
print(a.pow())

a = SafeFourCal(4,0)
print(a.div())

a = FourCal(4,2)
b = FourCal(4,2)

a.setdata(4,2)
print(a.first)

b.setdata(3,7)
print(b.first)

print(a.first)

print(id(a.first))
print(id(b.first))

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())