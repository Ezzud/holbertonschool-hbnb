from models.BaseModel import BaseModel

class Place(BaseModel):
    def __init__(self, owner = None, address = "", description = "", price = "", city = "", pictures = []):
        super().__init__()
        self.owner = owner
        self.address = address
        self.description = description
        self.price = price
        self.city = city
        self.pictures = pictures
    
    def get_owner(self):
        return self.owner
    
    def get_address(self):
        return self.address
    
    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_city(self):
        return self.city
    
    def get_pictures(self):
        return self.pictures

    def set_owner(self, newValue):
        self.owner = newValue

    def set_address(self, newValue):
        self.address = newValue

    def set_description(self, newValue):
        self.description = newValue

    def set_price(self, newValue):
        self.price = newValue

    def set_city(self, newValue):
        self.city = newValue
    
    def set_pictures(self, newValue):
        self.pictures = newValue
