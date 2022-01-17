import pdb
class student:
    def __init__(self, std):
        self.count = std
    def print_std(self):
        for i in range(self.count):
            print(i)
            pdb.set_trace()

if __name__=='__main__':
    student(5).print_std()
