class Booking:
    def __init__(self,bookingID,author,dest,startedAt,endAt,status):
        self.bookingID = bookingID
        self.author = author
        self.dest = dest
        self.startedAt = startedAt
        self.endAt = endAt
        self.status = status

    def get_booking(self):
        return self.bookingID
    
    def get_author(self):
        return self.author
    
    def get_dest(self):
        return self.author
    
    def get_dest(self):
        return self.dest
    
    def get_startedAt(self):
        return self.startedAt
    
    def get_endAt(self):
        return self.endAt
    
    def get_status(self):
        return self.status
    
    def set_booking(self, neWvalue):
        self.bookingID = neWvalue
    
    def set_author(self, neWvalue):
        self.author = neWvalue

    def set_dest(self, neWvalue):
        self.dest = neWvalue
    
    def set_startedAt(self, neWvalue):
        self.startedAt = neWvalue

    def set_endAt(self, neWvalue):
        self.endAt = neWvalue
    
    def set_status(self, neWvalue):
        self.status = neWvalue