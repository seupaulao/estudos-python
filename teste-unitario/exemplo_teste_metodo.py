import unittest

def fun(x):
    if x % 2 == 0:
       return x + 2
    else:
       return x + 1

class MyTest(unittest.TestCase):
    def test_se_impar(self):
        self.assertEqual(fun(3), 4)
    def test_se_par(self):
        self.assertEqual(fun(4), 6)

if __name__ == '__main__':
    unittest.main()
