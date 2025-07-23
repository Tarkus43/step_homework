from game import settings

def create_player():
    pass

def play_game():
    print('игра начата')

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