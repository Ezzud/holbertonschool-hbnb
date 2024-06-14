from models.BaseModel import BaseModel

class City(BaseModel):
        
    def __init__(self, name="", country_code=None):
        super().__init__()
        self.name = name
        self.country_code = country_code