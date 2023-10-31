import unittest
from maths import Maths
from parameterized import parameterized, parameterized_class

class TestMaths(unittest.TestCase):
    """ default test cases """
    def setUp(self) -> None:
        self.maths = Maths()
        
    @parameterized.expand([
        ((2, 3, 4), 9),
        ((2, 3, 2), 7),
        ((-0, 3), 3),
    ])

    def test_add(self, input, expected):
        self.assertEqual((self.maths.add(*input)), expected)
    
    @parameterized.expand([
        ("3, 'e', 'j'", (3, 'e', 'j'), TypeError),
        ("3, int('5')", (3, int('5')), TypeError)

    ])
    def test_add_raise(self, _, input, expected):
        self.assertRaises(expected, self.maths.add, input)
    
    def test_mul(self):
        self.assertEqual(self.maths.mul(2, 5), 10)
        self.assertRaises(TypeError, self.maths.mul, (3, 'e'))
    
    def test_mod(self):
        self.assertNotEqual(self.maths.mod(10, 2), 1)
        self.assertTrue(self.maths.mod(2, 2) == 0)
        self.assertRaises(TypeError, self.maths.mod, (4, 'e'))
    
    def test_div(self):
        self.assertEqual(self.maths.div(4, 2), 2)
        self.assertEqual(self.maths.div(4, 2), 2.00)
        self.assertRaises(ZeroDivisionError, self.maths.div, 5, 0)
    
    def test_pow(self):
        self.assertEqual(self.maths.pow(2,2), 4)
        self.assertNotEqual(self.maths.pow(3, 2), 5)
        self.assertRaises(TypeError, self.maths.pow, 'e', 2)
    

    def tearDown(self):
        """"""
if __name__ == '__main__':
    unittest.main()
