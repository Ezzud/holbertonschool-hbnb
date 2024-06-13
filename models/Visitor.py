class Visitor:
    def __init__(self, sessionID, addressID, visitDate):
            self.sessionID = sessionID
            self.addressID = addressID
            self.visitDate = visitDate
    
    def get_session(self):
        return self.sessionID

    def get_address(self):
        return self.addressID

    def get_visit_date(self):
        return self.visitDate

    def set_session(self, newSession):
        self.sessionID = newSession

    def set_address(self, newAddress):
        self.addressID = newAddress

    def set_visit_date(self, newDate):
        self.visitDate = newDate