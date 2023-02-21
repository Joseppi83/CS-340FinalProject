from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        """ Initialize MongoClient"""
        self.username = username
        self.password = password
        self.uriString = f'mongodb://{self.username}:{self.password}@127.0.0.1:47004/AAC'
        self.client = MongoClient(self.uriString)
        """ Get database for CRUD """
        self.database = self.client.get_database("AAC")

    def create(self, data: dict) -> bool:
        """ Create function"""
        """ Default behavior returns instance of InsertOneResult with insert id and bool T or F"""
        if data != None:
            didWork = self.database.animals.insert_one(
                data)
            return {True, didWork}
        else:
            raise Exception(
                "Nothing to save, because data parameter is empty or not a dictionary")

    def readAll(self):
        """ Read without arguments to query """
        didWork = self.database.animals.find({}, {"_id": 0})
        return didWork

    def readFilterWR(self):
        """ Read with  """
        """ Default behavior returns TypeError for fail and Cursor for success"""
        didWork = self.database.animals.find({"animal_type": "Dog", "breed": {"$in": [
            "Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]}, "sex_upon_outcome": "Intact Female", "age_upon_outcome_in_weeks": {"$gte": 26}, "age_upon_outcome_in_weeks": {"$lte": 156}}, {"_id": 0})
        return didWork

    def readFilterMWR(self):
        """ Read with  """
        """ Default behavior returns TypeError for fail and Cursor for success"""
        didWork = self.database.animals.find({"animal_type": "Dog", "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
                                              "sex_upon_outcome": "Intact Male", "age_upon_outcome_in_weeks": {"$gte": 26}, "age_upon_outcome_in_weeks": {"$lte": 156}}, {"_id": 0})
        return didWork

    def readFilterDIT(self):
        """ Read with  """
        """ Default behavior returns TypeError for fail and Cursor for success"""
        didWork = self.database.animals.find({"animal_type": "Dog", "breed": {"$in": [
            "Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]}, "sex_upon_outcome": "Intact Male", "age_upon_outcome_in_weeks": {"$gte": 20}, "age_upon_outcome_in_weeks": {"$lte": 300}}, {"_id": 0})
        return didWork

    def readOneKey(self, key: str, value):
        """ Read with key AND value """
        """ Default behavior returns TypeError for fail and Cursor for success"""
        if key != None and value != None:
            didWork = self.database.animals.find({key: value})
            return didWork

    def update(self, queryKey: str, queryValue: str, updateKey: str, updateValue: str):
        """ Update function """
        """ Default behavior returns TypeError for fail and Cursor for success"""
        if queryKey != None and queryValue != None and updateKey != None and updateValue != None:
            didWork = self.database.animals.update_one(
                {queryKey: queryValue}, {"$set": {updateKey: updateValue}})
            return didWork.raw_result

    def delete(self, key: str, value):
        """ Delete function """
        """ Default behavior returns TypeError for fail and Cursor for success"""
        if key != None and value != None:
            didWork = self.database.animals.delete_one({key: value})
            return didWork.raw_result
