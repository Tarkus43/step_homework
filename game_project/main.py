from game import settings
from game.game import Game
from game.models import Player,Enemy
from game.exceptions import EnemyDown,GameOver,WrongInput
from game import settings

def create_player() -> tuple[str,str]:
    while True:
        try:
            print('\n-- Поехали! --')
    
            player_name = input('\n-- Введите ваше имя! --\n---> ')
            difficulty = input('\n\n-- Введите сложность --\n-- Обычная -- 1\n-- Сложная -- 2\n---> ')

            if difficulty not in settings.MODES.keys():
                raise WrongInput
            
            print('\n\n-- Отлично! Тогда начнем! --')
            return (player_name,difficulty)
        
        except WrongInput:
            print('\n\n-- Неправильный ввод, попробуйте еще раз --\n')
            continue

def play_game():
    player_name,difficulty = create_player()
    game = Game(Player(player_name),difficulty)

    game.play()

def main():
    while True:
        user_input = input('-- Вас приветсвуют КАМЕНЬ НОЖНИЦЫ БУМАГА НАСМЕРТЬ --\n-- Начать игру --> 1\n-- Таблица лидеров --> 2\n-- Выход --> 3\n\n---> ')

        if user_input == '1':
            play_game()
        elif user_input == '2':
            pass
        elif user_input == '3':
            break
        else:
            print('-- !!!Неверный ввод, попробуйте еще раз!!! --')

main()