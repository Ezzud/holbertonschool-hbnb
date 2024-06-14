import importlib

module = importlib.import_module('managers.UserManager')
UserManager = getattr(module, 'UserManager')

user_manager = UserManager("data/users.json")