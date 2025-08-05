class PlayerRecord:

    def __init__(self,name:str,mode:int,score:int):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self,x) -> bool:
        pass

    def __str__(self):
        pass