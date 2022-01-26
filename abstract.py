from abc import ABC , abstractmethod

import math 
import random

#Student Name: NGUYEN TRI TIN (IIT)


class Sensor(ABC):

    @abstractmethod

    def __init__(self, Location :str):

        self._location = Location

        self._data = math.floor(random.random()*200)

        def getData(self):

            return self._data


class TempSensor(Sensor):

    def __init__(self, Location: str,types: str):

        super().__init__(Location)

        self._types= types
    def getTypes(self):

        return self._types
        
    def getData(self):

        return self._data

    def getLocation(self):

        return self._location
    

class DashBoard():

    def __init__(self,sensors):

        self.sensors = sensors 


    def printout(self):
        for sensor in self.sensors:

            print(f"location: {sensor.getLocation()}, tempt: {sensor.getData()}, types: {sensor.getTypes()}")

if __name__=="__main__":

    print("Program Started")

    myDash = DashBoard([

            TempSensor("Helsinki","C"),

            TempSensor("Lappeenranta","F")

    ])   
    myDash.printout()
print("Thanks for reading my code")