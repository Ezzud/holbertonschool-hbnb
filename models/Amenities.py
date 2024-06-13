class Amenities:
    def __init__(self,amenityID,name,description):
        self.amenityID = amenityID
        self.name = name
        self.description = description
    
    def get_amenity(self):
        return self.amenityID
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_amenity(self, neWvalue):
        self.amenityID = neWvalue
    
    def set_name(self, neWvalue):
        self.name = neWvalue
    
    def set_description(self, neWvalue):
        self.description = neWvalue