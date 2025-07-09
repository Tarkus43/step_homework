import settings
import random
import exceptions

class Player:
    # класс игрока, сущность

    lives:int = settings.PLAYER_LIVES
    score:int = 0

    def __init__(self, name:str):
        # игрок вписывает своё имя
        self.name = name

    def select_attack(self,atk:str):
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

    def add_score(self, scr:int):
        # добавляет очки игроку
        self.score += scr


class Enemy:
    # класс врага
    difficulty:str = settings.MODES['1']
    level:int = 1
    lives = settings.PLAYER_LIVES + level - 1 

    def __init__(self, level:int, diff:str):
        # инициализация
        self.level = level
        self.difficulty = diff
    
    def select_attack(self) -> str:
        # выбор атаки врагом
        return settings.ALLOWED_ATTACKS[str(random.randint(1,3))]
    
    def decrease_lives(self) -> exceptions.EnemyDown:
        # метод отнимающий жизни
        self.lives -= 1

        if self.lives <= 0:
            raise exceptions.EnemyDown
    

