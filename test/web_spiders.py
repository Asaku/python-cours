import unittest
import sys

sys.path.insert(0, '../WebSpiders')

from tools import extract as extract

class WebSpiders(unittest.TestCase):

    def test_extract(self):
        email = extract.extractEmail("qsdjkdqsd sdqsd email@email.fr dqsd qsdsddsddddss94qsd456")
        self.assertEqual(email, 'email@email.fr')

if __name__ == '__main__':
    unittest.main()
