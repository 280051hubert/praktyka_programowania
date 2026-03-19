import unittest
from stringkata import Add

class TestAdd(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(Add(""), 0)
    def test_addition(self):
        self.assertEqual(Add("5,6"), 11)
    def test_addition_multiple_numbers(self):
        self.assertEqual(Add("0,1,2,3,4,5"), 15)
    def test_multiple_line(self):
        self.assertEqual(Add("5\n6"), 11)
    def test_invalid_input_lines(self):
        with self.assertRaises(ValueError): #trzeba dac ValueError do Adda
            Add("0,\n")

if __name__ == "__main__":
    unittest.main()
