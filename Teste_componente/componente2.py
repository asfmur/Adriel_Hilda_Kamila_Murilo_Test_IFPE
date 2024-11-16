import unittest

def divisao(a,b):
    if b == 0:
        return False
    return a / b


class Test(unittest.TestCase):
    
    def test_divisao_por_zero(self):
        self.assertRaises(ZeroDivisionError)

if __name__ == '__main__':
    unittest.main()
