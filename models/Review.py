from models.BaseModel import BaseModel

class Review(BaseModel):

    def __init__(self, placeID = None, client = None, note = "", comment = ""):
        super().__init__()
        self.placeID = placeID
        self.client = client
        self.__note = note
        self.comment = comment
    
    def get_place(self):
        return self.placeID
    
    def get_client(self):
        return self.client
    
    def get_note(self):
        return self.__note

    def get_comment(self):
        return self.comment

    def set_place(self, newValue):
        self.placeID = newValue

    def set_client(self, newValue):
        self.client = newValue

    def set_note(self, newValue):
        self.__note = newValue

    def set_comment(self, newValue):
        self.comment = newValue
