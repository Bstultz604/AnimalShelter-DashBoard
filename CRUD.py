from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:54536/?authMechanism=DEFAULT&authSource=AAC'%('aac_user', 'user'))
        self.database = self.client['AAC']

    #Create method: used to generate new docuemnts in data base
    def createData(self, data):
        if data != None: 
            #'data' passed will be a dictionary
            self.database.animals.insert(data)
            return True

        else:
            raise Exception("Nothing to save :: Data parameter is empty")

    #Read Method: Data passed into fucntion will retrun first result
    def read_one(self, data):
        if data == None:
            raise Exception("Entries can not be found")

        else:
            return self.database.animals.find_one(data)

    #Read Method: Data passed into fucntion will retrun all matching results
    def read_all(self, data):
        if data == None:
            raise Exception("Entries can not be found")

        else:
             cursor = self.database.animals.find(data, {'_id': False})
             return cursor 


