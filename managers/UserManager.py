import json
import os

class UserManager:
    def __init__(self, dataPath):
        self.dataPath = dataPath
        self.userValues = None
        self.load_users()

    def load_users(self):
        if not os.path.exists(self.dataPath):
            self.userValues = "{}"
            self.save_users()
            return
        with open(self.dataPath, 'r+', encoding="utf-8") as file:
            self.userValues = json.load(file)
    
    def save_users(self):
        with open(self.dataPath, 'w+', encoding="utf-8") as file:
            json.dump(self.userValues, file)

    def get_user(self, user_id):
        parse = json.loads(self.userValues)
        print(parse)
        