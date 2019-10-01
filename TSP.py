import Utils
import City
from typing import List

class TSP:

    def __init__(self, cities : List[City.City], **dadosTSP):

        '''

        :param dadosTSP:
            CITIES: --> ARRAY DAS CIDADES
            distanceBetCities -->
        '''

        self.cities=cities
        self.goal=dadosTSP.get(Utils.Utils.GOAL)

    def getCities(self):
        return self.cities

    def getGoal(self):
        return self.goal

    def setNewGoal(self,newGoal):
        self.goal=newGoal

    def distanceBetweenTwoCities(self, actualCity : City.City, neighborCity: City.City):

        numberLines=len(actualCity)/2

        for i in range(numberLines):
            for j in 0:
                if actualCity.getCityNeighbors()[i][j] == neighborCity.getName():
                    return actualCity.getCityNeighbors()[i][1]
        return -1