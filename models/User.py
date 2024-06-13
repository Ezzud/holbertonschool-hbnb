class User:
    def __init__(self, userID, name, email, password, address, phone):
        self.userID = userID
        self.name = name
        self.email = email
        self.__password = password
        self.address = address
        self.phone = phone
    
    def get_userid(self):
        return self.userID
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.__password

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone
    
    def set_userid(self, newValue):
        self.userID = newValue

    def set_name(self, newValue):
        self.name = newValue

    def set_email(self, newValue):
        self.email = newValue

    def set_password(self, newValue):
        self.__password = newValue

    def set_address(self, newValue):
        self.address = newValue

    def set_phone(self, newValue):
        self.phone = newValue
