# consts
LOW = "1"
MEDIUM = "2"
HIGH = "3"
STATUS = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}
TODO_DICT = {'name':None, 'descr':None, 'id':None, 'prio':None, 'status':None}
KEYS = ['name', 'descr', 'id', 'prio', 'status']
EXAMPLE = 'name/description of todo/1/3/high'             

# changes todo from string format to dict format so python can easily work with it
def todo_to_dict(todo:str) -> dict:
    todo_list = todo.split('/')
    todo_dict = dict(zip(KEYS,todo_list))
    todo_dict['id'] = int(todo_dict['id'])
    return todo_dict

# changes todo in dict format to string format for reading or adding to txt file
def dict_to_todo(todo:dict[str:str,str:str,str:int,str:int,str:str]) -> str:
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
            if todo_to_dict(line)['id'] > int(max_id):
                max_id = line.split('/')[2]
    return int(max_id)  

# gets todo in str type by id
def get_todo(id:int) -> str:
    if id > get_last_id():
        return 'ERROR: id does not exist'
    with open('db.txt','r') as file:
        for line in file:
            if todo_to_dict(line)['id'] == id:
                return line

# gets next id
def next_id():
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

def change_todo(id: int, param: str, text: str) -> str:
    todo_list = []
    with open('db.txt', 'r') as file:
        for line in file:
            todo_list.append(todo_to_dict(line.strip()))

    for todo in todo_list:
        if todo['id'] == id:
            todo[param] = text
            break

    with open('db.txt', 'w') as file:
        for todo in todo_list:
            file.write(dict_to_todo(todo) + '\n')


change_todo(1,'descr','i tested this shit nigga')    


