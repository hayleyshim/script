import check_condition
import unittest

class Test_if(unittest.TestCase):
    def test_if(self):
        result = check_condition.check_if()
        self.essertEqual(result, 20)
if __name__=='__main__':
    unittest.main()
