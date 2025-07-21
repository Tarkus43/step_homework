import unittest
import random
from unittest.mock import Mock
from unittest.mock import patch
from game.models import Player,Enemy


class TestPlayer(unittest.TestCase):
        
    player = Player('Victor')

    def test_init(self):
        self.assertEqual(Player('Victor').name,self.player.name,'players name should be Victor')

    @patch('builtins.input',return_value='1')
    def test_select_attack_stone(self, mock_input):
        self.assertEqual(self.player.select_attack(),'Stone','should be Stone')
    
    @patch('builtins.input',return_value='2')
    def test_select_attack_scissors(self, mock_input):
        self.assertEqual(self.player.select_attack(),'Scissors','should be Scissors')

    @patch('builtins.input',return_value='3')
    def test_select_attack_stone(self, mock_input):
        self.assertEqual(self.player.select_attack(),'Paper','should be Paper')

    @patch('game.models.print')
    @patch('game.models.input',side_effect=['aboba','1'])
    def test_select_attack_wrong_input(self, mock_input, mock_print):

        result = self.player.select_attack()

        self.assertEqual(result, 'Stone')

        mock_print.assert_called_with('-- !!!Неверный ввод, попробуйте еще раз!!! --')


if __name__ == '__main__':
    unittest.main()


