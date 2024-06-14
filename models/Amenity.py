from models.BaseModel import BaseModel 

class Amenity(BaseModel):

    amenities = set()

    def __init__(self, name="", description="", place_id=""):
        super().__init__()
        self.name = name
        self.description = description
        self.place_id = place_id
        self.amenities.add(name)