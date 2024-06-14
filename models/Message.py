from models.BaseModel import BaseModel 

class Message(BaseModel): 
    def __init__(self, author = None, dest = None, content = ""):
        super().__init__()
        self.author = author
        self.dest = dest
        self.content = content
    
    def get_author(self):
        return self.author
    
    def get_dest(self):
        return self.dest
    
    def get_content(self):
        return self.content

    def set_author(self, neWvalue):
        self.author = neWvalue
    
    def set_dest(self, neWvalue):
        self.dest = neWvalue

    def set_content(self, neWvalue):
        self.content = neWvalue