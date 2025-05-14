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

def get_last_id() -> int:
    max_id = 0
    with open('db.txt','r') as db:
        for line in db:
            if int(line.split('/')[2]) > int(max_id):
                max_id = line.split('/')[2]
    return max_id            

print(get_last_id())                