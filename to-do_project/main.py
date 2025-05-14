LOW = "1"
MEDIUM = "2"
HIGH = "3"
STATUS = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}

def add_todo(name:str, text:str,prio:int,status) -> None:
    with open('db.txt','r') as db:
        id = None
        for line in db:
            id = int(line) + 1 
            break
    with open('db.txt','a') as db:
        db.write('\n' + f'{name}/{text}/{id}/{prio}/{status}')

add_todo('new todo','im gonna to test this func',HIGH,STATUS[HIGH],)                    