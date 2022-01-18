import arithmatic
import unittest

class test_addition(unittest.TestCase):
    def test_add_number_int(self):
        sum = arithmatic.add_number(10, 20)
        self.asserEqual(sum, 30)


    def test_add_number_float(self):
        sum = arithmatic.add_number(10.5, 20)
        self.asserEqual(sum, 30.5)

if __name__ == '__main__':
    unittest.main()