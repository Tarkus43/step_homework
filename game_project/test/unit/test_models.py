import unittest
import random
from unittest.mock import Mock
from unittest.mock import patch
from game.models import Player,Enemy
from game.exceptions import GameOver,EnemyDown
from game import settings


class TestPlayer(unittest.TestCase):
        
    player = Player('Victor')
    player.lives = 2

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

    def test_decrease_lives(self):
        player = Player('tarkus')
        player.lives = 2
        player.decrease_lives()
        self.assertEqual(player.lives,1,'should be 1')


    def setUp(self):
        self.player.decrease_lives()

    def test_decrease_lives_gameover(self):
        with self.assertRaises(GameOver):
            self.player.decrease_lives()
    
    def tearDown(self):
        self.player.lives = 2

    def test_add_score(self):
        self.player.add_score(1)

        self.assertEqual(self.player.score, 1, 'should be 1')


class TestEnemy(unittest.TestCase):
    
    def test_init_level(self):
        enemy = Enemy(1,'1')
        self.assertEqual(enemy.level,1,'should be 1')
    
    def test_init_difficulty(self):
        enemy = Enemy(1,'1')
        self.assertEqual(enemy.difficulty,1,'should be 1')
    
    def test_init_lives(self):
        enemy = Enemy(1,'1')
        self.assertEqual(enemy.lives,settings.PLAYER_LIVES,'should be 2')
    
    def test_init_bigger_level(self):
        enemy = Enemy(2,'1')
        self.assertEqual(enemy.lives,settings.PLAYER_LIVES + enemy.level - 1 ,'should be 3')
    

    def test_decrease_lives_enemy(self):
        enemy = Enemy(1,'1')
        enemy.decrease_lives()
        self.assertEqual(enemy.lives,1,'should be 1')

    def test_decrease_lives_EnemyDown(self):
        with self.assertRaises(EnemyDown):
            enemy = Enemy(1,'1')
            enemy.decrease_lives()
            enemy.decrease_lives()


if __name__ == '__main__':
    unittest.main()


