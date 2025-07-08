from game import settings

def create_player():
    pass

def play_game():
    pass

def main():
    while True:
        user_input = input('-- Вас приветсвуют КАМЕНЬ НОЖНИЦЫ БУМАГА НАСМЕРТЬ --\n-- Начать игру -->1\nТаблица лидеров --> 2\nВыход --> 3\n---> ')

        if user_input in settings.MENU_OPTIONS.keys():
            play_game()
        else:
            print('-- !!!Неверный ввод, попробуйте еще раз!!! --')

