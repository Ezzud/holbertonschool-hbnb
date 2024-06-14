from persistence.IPersistenceManager import IPersistenceManager
from models.BaseModel import BaseModel
from models.users import Users
from models.city import City
from models.country import Country
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DataManager(IPersistenceManager):
    storage = {}

    def save(self, entity):
        try:
            if isinstance(entity, BaseModel):
                user = entity.__dict__
                class_type = entity.__class__.__name__

                if class_type in DataManager.storage.keys():
                    DataManager.storage[class_type].append(user)
                else:
                    DataManager.storage[class_type] = [user]
                return user
            else:
                raise TypeError()
        except TypeError:
            print("The argument should be an object")

    def get(self, entity_id, entity_type):
        try:
            for user in DataManager.storage[f"{entity_type}"]:
                if user["id"] == entity_id:
                    return user
        except Exception as e:
            print(e)

    def update(self, entity):
        class EntityNotFoundError(Exception):
            pass

        try:
            class_type = f"{entity.__class__.__name__}"
            print(entity.id)
            for idx, user in enumerate(DataManager.storage[class_type]):
                if user["id"] == entity.id:
                    DataManager.storage[class_type][idx] = entity.__dict__
                    return entity.__dict__
            raise EntityNotFoundError("Bad Request")
        except EntityNotFoundError as e:
            raise e
        except Exception as e:
            print(e)

    def delete(self, entity_id, entity_type):
        try:
            DataManager.storage[f"{entity_type}"] = [user for user in DataManager.storage[f"{entity_type}"] if user["id"] != entity_id]
        except Exception as e:
            print(e)