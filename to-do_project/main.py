LOW = "1"
MEDIUM = "2"
HIGH = "3"
STATUS = {
    LOW: "low",
    MEDIUM: "medium",
    HIGH: "high"
}

def add_to_db(text):
    with open('db.txt','a') as db:
        db.write('\n' + text)
