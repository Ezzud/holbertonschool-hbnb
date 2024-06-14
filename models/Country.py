from models.BaseModel import BaseModel 

class Country(BaseModel):

    countries = set()

    def __init__(self, name="", population=0, code=None):
        super().__init__()
        self.name = name
        self.population = population
        self.code = code
        self.countries.add(code)