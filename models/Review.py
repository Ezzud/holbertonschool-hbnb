class Review:
    def __init__(self, reviewID, placeID, client, note, comment, date):
        self.reviewID = reviewID
        self.placeID = placeID
        self.client = client
        self.__note = note
        self.comment = comment
        self.date = date
    
    def get_review(self):
        return self.reviewID
    
    def get_place(self):
        return self.placeID
    
    def get_client(self):
        return self.client
    
    def get_note(self):
        return self.__note

    def get_comment(self):
        return self.comment

    def get_date(self):
        return self.date
    
    def set_review(self, newValue):
        self.reviewID = newValue

    def set_place(self, newValue):
        self.placeID = newValue

    def set_client(self, newValue):
        self.client = newValue

    def set_note(self, newValue):
        self.__note = newValue

    def set_comment(self, newValue):
        self.comment = newValue

    def set_date(self, newValue):
        self.date = newValue
