import unittest

from ch2_unit_test.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        # print "Hello"
        # self.assertEqual(4, self.calc.add("Hello", "World"))
        self.assertAlmostEqual(1, 1)

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")

    def test_assert_raises(self):
        self.assertRaises(ValueError, int, "a")

    def test_assert_raises_alternative(self):
        with self.assertRaises(AttributeError):
            [].get


if __name__ == '__main__':
    unittest.main()
