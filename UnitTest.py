import unittest
import L7_MaxDoubleSlice

class UnitTest(unittest.TestCase):

    def test_3_element_a(self):
        A = [5,5,5]
        self.assertEqual(L7_MaxDoubleSlice.solu(A), 0)
    def test_3_element_b(self):
        A = [5,-45,-50]
        self.assertEqual(L7_MaxDoubleSlice.solu(A), 0)

    def test_normal_a(self):
        A = [3,2,6,-1,4,5,-1,2]
        self.assertEqual(L7_MaxDoubleSlice.solu(A), 17)
    def test_normal_b(self):    
        A = [-2, -4, -3, 5, 8, 4, -25, -2, -1, 6, 8, 7, -4, -5, -7, 3, 4, -6, -4, 10, -8, -1, 21, 8, 2]
        self.assertEqual(L7_MaxDoubleSlice.solu(A), 45)



if __name__ == '__main__':
    unittest.main()