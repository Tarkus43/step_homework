
# consts
HIGH = "1"
MEDIUM = "2"
LOW = "3"
PRIORITY = {
    LOW:"Высокий",
    MEDIUM: "Средний",
    HIGH: "Низкий"
}
STATUS = {
    LOW: "Новый",
    MEDIUM: "В процессе",
    HIGH: "Выполнено или заброшено"
}
TODO_DICT = {'name':None, 'descr':None, 'id':None, 'prio':None, 'status':None}
KEYS = ['name', 'descr', 'id', 'prio', 'status']
EXAMPLE = 'name/description of todo/1/3/3'             


# makes from all todos one list of them
def todos_to_list() -> list[dict]:
    todo_list = []
    with open('db.txt', 'r') as file:
        for line in file:
            todo_list.append(todo_to_dict(line.strip()))
    return todo_list

# changes todo from string format to dict format so python can easily work with it
def todo_to_dict(todo:str) -> dict:
    if todo == None:
        return todo
    todo = todo.strip()
    if len(todo) < 9:
        return None
    todo_list = todo.split('/')
    todo_dict = dict(zip(TODO_DICT.keys(),todo_list))
    todo_dict['id'] = int(todo_dict['id'])
    return todo_dict


# changes todo in dict format to string format for reading or adding to txt file
def dict_to_todo(todo:dict[str:str,str:str,str:int,str:int,str:str]) -> str:
    if todo == None:
        return None
    return '/'.join([str(x) for x in todo.values()])


# adds todo to txt file
def add_todo(todo:dict) -> None:
    with open('db.txt','a') as db:
        db.write('\n'+  dict_to_todo(todo) )


# gets highest id to find last todo
def get_last_id() -> int:
    max_id = 0
    with open('db.txt','r') as db:
        for line in db:
            if len(line) < 9:
                continue
            if todo_to_dict(line)['id'] > int(max_id):
                max_id = line.split('/')[2]
    return int(max_id)  


# gets todo in str type by id
def get_todo(id:int) -> str:
    if id > get_last_id():
        return None
    with open('db.txt','r') as file:
        for line in file:
            if todo_to_dict(line) == None:
                continue
            if todo_to_dict(line)['id'] == id:
                return line
        else: return 'todo with such id does not exist'


# gets next id
def next_id() -> int:
    return get_last_id() + 1


# finds todos by keyword
def find_todo(key_word:str) -> list[dict]:
    todo_list = []
    with open('db.txt','r') as file:
        for todo in file:
            line = todo_to_dict(todo.strip())
            if not line:
                continue
            if key_word in line['name'] or key_word in line['descr']:
                todo_list.append(line)
    if len(todo_list) == 0:
        return None
    else:
        return todo_list


# changing todo and rewriting it to file
def change_todo(id: int, param: str, text: str) -> str:
    try:
        if param not in  ['name', 'descr','prio','status']:
            raise NameError 
        todo_list = todos_to_list()

        for todo in todo_list:
            if todo['id'] == id:
                todo[param] = text
                break

        with open('db.txt', 'w') as file:
            for todo in todo_list:
                file.write(dict_to_todo(todo) + '\n')
    except NameError:
        print('wrong parameter')


# deleting todo from txt file
def delete_todo(id:int) -> str:
    try:
        if get_todo(id) == 'ERROR: id does not exist':
            raise IndexError
        todo_list = []
        with open('db.txt', 'r') as file:
            for line in file:
                todo_list.append(todo_to_dict(line.strip()))
    
        for i in range(len(todo_list)):
            if todo_list[i]['id'] == id:
                del todo_list[i]
                break
    
        with open('db.txt', 'w') as file:
            for todo in todo_list:
                file.write(dict_to_todo(todo) + '\n')
    except IndexError:
        print('wrong id')
        raise IndexError

# sorting todos by some parameter
def sort_todos(param:str) -> list[dict]:
    flag = None
    if param == 'prio':
        flag = True
    elif param == 'status' or  param == 'id':
        flag == False
    return sorted(todos_to_list(), key=lambda x: int(x[param]), reverse=flag)

# printing todos for user
def print_todos(todo_list:list[dict]) -> str:
    if todo_list == None:
        print('\nТакой задачи нет')
        return None
    if type(todo_list) == list:
        for i in range(len(todo_list)):
            print(f'\nНазвание задачи: {todo_list[i]['name']}')
            print(f'Описание задачи: {todo_list[i]['descr']}')
            print(f'Приоритет задачи: {PRIORITY[todo_list[i]['prio']]}')
            print(f'Статус задачи: {STATUS[todo_list[i]['status']]}')

    else:
        print(f'\nНазвание задачи: {todo_list['name']}')
        print(f'\n Описание задачи: {todo_list['descr']}')
        print(f'\nПриоритет задачи: {PRIORITY[todo_list['prio']]}')
        print(f'\nСтатус задачи: {STATUS[todo_list['status']]}')


# cleaning from empty lines in file
def clean():
    with open('db.txt', 'r') as file:
        lines = [x for x in file]

    cleaned_lines = [x for x in lines if x.strip() != '']

    with open('db.txt', 'w') as file:
        file.writelines(cleaned_lines)

# interface 
def main():
    while True:
        user_input = input('\n-- Добавить задачу --> 1 \n-- Просмотреть задачи --> 2 \n-- Обновить задачу --> 3 \n-- Удалить задачу --> 4 \n-- Выйти из программы --> 0 \n -->').strip()
        
        match user_input:
            case '0':
                print('завершение...')
                print('завершено')

                break
            
            
            case '1':
                name = input('--Введите имя задачи! \n--> ').strip()
                descr = input('--Введите описание задачи! \n--> ').strip()
                prio = input('--Введите приоритет задачи! \n1, 2 или 3 где 1 самый высокий \n--> ').strip()
                status = input('--Введите cтатус задачи! \nновая: 1 \nв процессе: 2 \nзаброшено, выполнено: 3 \n--> ').strip()
                if prio == '1' or prio == '2' or prio == '3':
                    if status == '1' or status == '2' or status == '3':
                        add_todo({'name':name, 'descr':descr, 'id':next_id(), 'prio':prio, 'status':status})
                        print('\n--задача успешно добавлена\n!')
                        clean()
                    else: 
                        print('--некоректный статус')
                        continue
                else:
                    print("--некорректный приоритет")
                    continue
            
            case '2':
                user_input = input('\n-- Отобразить задачи в изначальном виде --> 1 \n-- Отсортировать по статусу --> 2 \n-- Отсортировать по приоритету --> 3 \n-- Осуществить поиск по названию или описанию --> 4 \n -->').strip()
                match user_input:
                    case '1':
                        print('')
                        print_todos(todos_to_list())
                        print('')
                    
                    case '2':
                        print('')
                        print_todos(sort_todos('status'))
                        print('')

                    case '3':
                        print('')
                        print_todos(sort_todos('prio'))
                        print('')
                    
                    case '4':
                        user_input = input('\n-- Введите ключевое слово для поиска --> ')
                        print_todos(find_todo(user_input))

                    case _:
                        print('\n!!!Неправильный ввод, попробуйте еще раз!!!')
            
            case '3': 
                id = int(input('\n-- Введите ID задачи --> ').strip())
                if print_todos(todo_to_dict(get_todo(id))) == None:
                    print('Неправильный ID')
                    continue
                print_todos(todo_to_dict(get_todo(id)))
                user_input_menu = input('\n-- название --> 1\n-- описание --> 2\n-- приоритет --> 3\n-- статус --> 4 \n-->').strip()

                match user_input_menu:
                    case '1':
                        user_input = input('\n-- Введите новое название -->')
                        change_todo(id, 'name', user_input)
                    case '2':
                        user_input = input('\n-- Введите новое описание -->')
                        change_todo(id, 'descr', user_input)
                    case '3':
                        while True:
                            user_input = input('\n-- Введите новый приоритет \n1, 2 или 3 где 1 самый высокий \n-->').strip()
                            if user_input not in PRIORITY.keys():
                                print('Неправильный ввод, попробуйте еще раз!')
                                continue   
                            change_todo(id, 'prio', user_input)
                            break
                    case '4':
                         while True:
                            user_input = input('\n-- Введите новый статус \nновая: 1 \nв процессе: 2 \nзаброшено, выполнено: 3 \n--> ').strip()
                            if user_input not in STATUS.keys():
                                print('Неправильный ввод, попробуйте еще раз!')
                                continue   
                            change_todo(id, 'status', user_input)
                            break
                    
                    case _:
                        print('Неправильный ввод, попробуйте еще раз!')    

            case '4': 
                id = int(input('\n-- Введите ID задачи --> ').strip())
                if get_todo(id) == None:
                    print('Неправильный ID')
                    continue
                delete_todo(id)
                print('Задача успешно удалена!')

            case _:
                print('Неправильный ввод, попробуйте еще раз!')

main()

