from datetime import datetime
import uuid

class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.createdAt = str(datetime.now())
        self.updatedAt = str(datetime.now())
    
    def get_id(self):
        return self.id
    
    def get_creation(self):
        return self.createdAt

    def get_update(self):
        return self.updatedAt