import settings

class Player:
    # класс игрока, сущность

    lives = settings.PLAYER_LIVES
    score = 0

    def __init__(self, name:str):
        # игрок вписывает своё имя
        self.name = name

    def select_attack(self,atk:str):
        # игрок выбирает атаку, заставит ввести пока не будет валидное значение
        pass
    
    def decrease_lives(self):
        # если игрок проигрывает бой - то он теряет жизни
        self.lives -= 1

    def add_score(self,scr:int):
        # добавляет очки игроку
        self.score += scr




        

