import unittest
from unittest.mock import Mock
from game.models import Player,Enemy
# from game.exceptions import EnemyDown,GameOver

class TestPlayer(unittest.TestCase):

    def test_init(self):
        player = Player('Victor')
        self.assertEqual(Player('Victor').name,player.name,'players name should be Victor')


if __name__ == '__main__':
    unittest.main()


