import models
import settings
import exceptions



class Game():
    # класс игры
    player: models.Player
    enemy: models.Enemy

    
    def __init__(self,player:models.Player,difficulty):
        # инициализация
        self.player = player

        if difficulty in int(settings.MODES.keys):
            self.difficulty = difficulty
        else:
            print('неправильный ввод!')

        self.enemy = models.Enemy
    
    
    
    def fight(self) -> int:
        # бой 
        player_input = self.player.select_attack()
        enemy_input = self.enemy.select_attack()
        return settings.ATTACK_PAIRS_OUTCOME[(player_input,enemy_input)]


    
    def handle_fight_result(self,result:int):
        # обработчик боя
        if result == 1:
            self.enemy.decrease_lives()
        elif result == 0:
            print('-- ничья! --')
        elif result == -1:
            self.player.decrease_lives()
        else:
            raise ValueError

        if self.player.lives == 0:
            raise exceptions.GameOver
        if self.enemy.lives == 0:
            raise exceptions.EnemyDown       

    
    def save_score(self):
        # метод сохраняющий счёт
        pass

    
    def new_enemy(self):
        # создание нового врага
        if hasattr(self, 'enemy'):
            level = self.enemy.level + 1
        else:
            level = 1
        self.enemy = models.Enemy(level,self.difficulty)
    
    def play(self):
        # процесс игры
        while True:
            try:
                self.fight()
                self.handle_fight_result()
            
            except exceptions.EnemyDown:
                self.player.score += 1
                self.new_enemy()
            except exceptions.GameOver:
                self.save_score()