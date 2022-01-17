class student:
    def __init__(self,std):
        self.count = std
    def go(self):
        for i in range(self.count):
            print(i)
        return
if __name__ == "__main__":
    student(5).go()

