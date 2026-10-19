import unittest
from app import add

class T(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()


class T2(unittest.TestCase):
    def test_subtract(self):
        from app import subtract
        self.assertEqual(subtract(5, 2), 3)
