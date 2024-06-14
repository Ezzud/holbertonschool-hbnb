from models.BaseModel import BaseModel 

class Visitor(BaseModel):
    def __init__(self, addressID = "", visitDate = None):
        super().__init__()
        self.addressID = addressID
        self.visitDate = visitDate

    def get_address(self):
        return self.addressID

    def get_visit_date(self):
        return self.visitDate

    def set_address(self, newAddress):
        self.addressID = newAddress

    def set_visit_date(self, newDate):
        self.visitDate = newDate