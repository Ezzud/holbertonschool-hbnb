class Country:
    def __init__(self,countryID,name):
        self.countryID = countryID
        self.name = name

    def get_country(self):
        return self.countryID

    def get_name(self):
        return self.name
    
    def set_country(self, newValue):
        self.countryID = newValue

    def set_name(self, neWvalue):
        self.name = neWvalue