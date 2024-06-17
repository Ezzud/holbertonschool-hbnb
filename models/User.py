from models.BaseModel import BaseModel
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class User(BaseModel):

    emails = set()

    def __init__(self, email='', password='', first_name='', last_name='', review_id=[], place_id=[]):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.review_id = review_id
        self.place_id = place_id
        if(re.fullmatch(regex, email)):
            pass
        else:
            raise ValueError('Invalid Email')
            
            
