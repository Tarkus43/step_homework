import unittest
from unittest.mock import Mock
from game import models

class TestPlayer(unittest.TestCase):

    def test_init(self):
        player = models.Player()
        player.name = 'Victor'
        self.assertEqual(models.Player('Victor'),player,'players name should be Victor')

if __name__ == '__main__':
    unittest.main()


