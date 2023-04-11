import unittest
class TestNumeracion(unittest.TestCase):

    def test_binario2decimal(self):
        self.assertEqual( binario2decimal("010111000", 92))
    
    def test_binario2decimal(self):
        self.assertEqual( decimal2binario(97), ("01100001"))
    
if __name__ == '__main__':
    unittest.main()