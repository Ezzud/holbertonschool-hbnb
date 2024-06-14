from models.BaseModel import BaseModel 

class Booking(BaseModel):
    def __init__(self, author = None, dest = None, startedAt = None, endAt = None, status = ""):
        super().__init__()
        self.author = author
        self.dest = dest
        self.startedAt = startedAt
        self.endAt = endAt
        self.status = status
    
    def get_author(self):
        return self.author
    
    def get_dest(self):
        return self.author
    
    def get_dest(self):
        return self.dest
    
    def get_startedAt(self):
        return self.startedAt
    
    def get_endAt(self):
        return self.endAt
    
    def get_status(self):
        return self.status
    
    def set_author(self, neWvalue):
        self.author = neWvalue

    def set_dest(self, neWvalue):
        self.dest = neWvalue
    
    def set_startedAt(self, neWvalue):
        self.startedAt = neWvalue

    def set_endAt(self, neWvalue):
        self.endAt = neWvalue
    
    def set_status(self, neWvalue):
        self.status = neWvalue