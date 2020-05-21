from database.mongoConnection import MongoConection
from json import JSONEncoder

import pprint

class Temperature(JSONEncoder):

    day = ""
    time = ""
    position = ""
    temp = 0

    @staticmethod
    def create(temperrature):
        db = MongoConection.getDatabase()
        result = db.temperature.insert_one(temperrature)
        return True

    @staticmethod
    def getByDay(day):
        temperatures = []
        db = MongoConection.getDatabase()
        print("getByDay: ")

        temps = db.temperature.find({"day": day})

        for temp in temps:
            pprint.pprint(temp)

            temperature = Temperature()
            temperature.day = temp["day"]
            temperature.time = temp["time"]
            temperature.position = temp["position"]
            temperature.temp = temp["temp"]

            temperatures.append(temperature)

        return temperatures

    def toJSON(self):
        return {'day': self.day,
                'time': self.time,
                'position': self.position,
                'temp': self.temp
                }


        