import unittest
import L8_Peak

class UnitTest(unittest.TestCase):

    def test_3_element(self):
        A = [5,7,5]
        self.assertEqual(L8_Peak.solution(A), 1)
    def test_1_element(self):
        A = [5]
        self.assertEqual(L8_Peak.solution(A), 0)
    def test_12_element(self):
        A = [1,2,3,4,3,4,1,2,3,4,6,2]
        self.assertEqual(L8_Peak.solution(A), 3)


if __name__ == '__main__':
    unittest.main()