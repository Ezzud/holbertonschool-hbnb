from models.BaseModel import BaseModel 

class Amenities(BaseModel):
    amenities = set()

    def __init__(self, name = "", description = ""):
        super().__init__()
        self.name = name
        self.description = description
        self.amenities.add(name)
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_name(self, neWvalue):
        self.name = neWvalue
    
    def set_description(self, neWvalue):
        self.description = neWvalue