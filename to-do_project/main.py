
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
    LOW: "новый",
    MEDIUM: "в процессе",
    HIGH: "выполнено или заброшено"
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
        db.write('\n' + dict_to_todo(todo))


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
        return 'ERROR: id does not exist'
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
            if key_word in todo_to_dict(todo)['name'] or key_word in todo_to_dict(todo)['descr']:
                todo_list.append(todo_to_dict(todo))
    if len(todo_list) == 0:
        return 'Did not found'
    else:
        return todo_list


# changing todo and rewriting it to file
def change_todo(id: int, param: str, text: str) -> str:
    try:
        if param != 'name' and param != 'descr':
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

# interface 
def main():
    while True:
        user_input = input('Добавить задачу: 1 \nПросмотреть задач: 2 \nОбновить задачу : 3 \nУдалить задачу: 4 \nВыйти из программы: 0 \n -->')
        match user_input:
            case '0':
                print('завершение...')
                print('завершено')

                break
            case '1':
                name = input('Введите имя задачи! \n--> ')
                descr = input('Введите описание задачи! \n--> ')
                prio = input('Введите приоритет задачи! \n1, 2 или 3 где 3 самый высокий \n--> ')
                status = input('Введите cтатус задачи! \nновая: 1 \nв процессе: 2 \nзаброшено, выполнено: 3 \n--> ')
                if prio == '1' or prio == '2' or prio == '3':
                    if status == '1' or status == '2' or status == '3':
                        add_todo({'name':name, 'descr':descr, 'id':next_id(), 'prio':prio, 'status':status})
                        print('\nзадача успешно добавлена\n!')
                    else: 
                        print('некоректный статус')
                        continue
                else:
                    print("некорректный приоритет")
                    continue

print_todos(todo_to_dict(EXAMPLE))


