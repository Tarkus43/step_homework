import random
from unittest.mock import Mock
from .exceptions import EnemyDown, GameOver
from . import settings


class Player:
    # класс игрока, сущность

    lives:int = settings.PLAYER_LIVES
    score:int = 0

    def __init__(self, name:str):
        # игрок вписывает своё имя
        self.name = name

    def select_attack(self):
        # игрок выбирает атаку, заставит ввести пока не будет валидное значение
            while True:
                user_input = input('-- Выбор атаки -- \n-- камень --> 1\n-- ножницы --> 2 \n-- бумага --> 3\n---> ')
                if user_input in settings.ALLOWED_ATTACKS.keys():
                    return settings.ALLOWED_ATTACKS[user_input]
                else:
                    print('-- !!!Неверный ввод, попробуйте еще раз!!! --')
    
    def decrease_lives(self):
        # если игрок проигрывает бой - то он теряет жизни
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver

    def add_score(self, scr:int):
        # добавляет очки игроку
        self.score += scr


class Enemy:
    # класс врага
    difficulty:int = 1
    level:int = 1

    def __init__(self, level:int, diff:str):
        # инициализация
        self.level = level
        self.difficulty = int(diff)
        self.lives = settings.PLAYER_LIVES + level + self.difficulty - 2 
    
    def select_attack(self) -> str:
        # выбор атаки врагом
        return settings.ALLOWED_ATTACKS[str(random.randint(1,3))]
    
    def decrease_lives(self) -> None:
        # метод отнимающий жизни
        self.lives -= 1

        if self.lives <= 0:
            raise EnemyDown
    