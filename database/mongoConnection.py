from pymongo import MongoClient

class MongoConection:

    @staticmethod
    def getConnection():
        client = MongoClient('localhost', 27017)
        return client

    @staticmethod
    def getDatabase():
        client = MongoClient('localhost', 27017)
        database = client.iot
        return database
