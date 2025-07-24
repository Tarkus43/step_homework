from .models import Player,Enemy
from . import settings
from . import exceptions



class Game():
    # класс игры
    player: Player
    enemy: Enemy

    
    def __init__(self,player:Player,difficulty:str):
        # инициализация
        self.player = player

        if difficulty in settings.MODES.keys():
            self.enemy = Enemy(1,difficulty)
            self.difficulty = difficulty
        else:
            print('неправильный ввод!')

        
    
    
    
    def __fight(self) -> int:
        # бой 
        player_input = self.player.select_attack()
        enemy_input = self.enemy.select_attack()
        return settings.ATTACK_PAIRS_OUTCOME[(player_input,enemy_input)]


    
    def __handle_fight_result(self,result:int):
        # обработчик боя
        if result == 1:
            print('\n-- Победа! --\n')
            self.enemy.decrease_lives()
        elif result == 0:
            print('\n-- Ничья! --\n')
        elif result == -1:
            print('\n-- Поражение --\n')
            self.player.decrease_lives()
        else:
            raise ValueError

        if self.player.lives == 0:
            raise exceptions.GameOver
        if self.enemy.lives == 0:
            raise exceptions.EnemyDown       

    
    def __save_score(self):
        # метод сохраняющий счёт
        pass

    
    def __new_enemy(self):
        # создание нового врага
        if hasattr(self, 'enemy'):
            level = self.enemy.level + 1
        else:
            level = 1
        self.enemy = Enemy(level,self.difficulty)
    
    def play(self):
        # процесс игры
        while True:
            try:
                self.__handle_fight_result(self.__fight())
                print(f'-- Ваше здоровье: {self.player.lives} --')
                print(f'-- У противника осталось {self.enemy.lives} очков здоровья! --')
            
            except exceptions.EnemyDown:
                self.player.score += 1
                self.__new_enemy()
                self.player.lives = 2
                print('\n-- вы победили --\n-- новый противник! --')
            
            except exceptions.GameOver:
                print('\n-- ИГРА ОКОНЧЕНА --')
                self.__save_score()
                break