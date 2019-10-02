import Utils
import City
from typing import List

class TSP:

    def __init__(self, cities : List[City.City]):

        '''

        :param dadosTSP:
            CITIES: --> ARRAY DAS CIDADES
            distanceBetCities -->
        '''

        self.cities=cities

    def getCities(self):
        return self.cities

    def distanceBetweenTwoCities(self, actualCity : City.City, neighborCity: City.City):

        numberLines=len(actualCity)/2

        for i in range(numberLines):
            for j in 0:
                if actualCity.getCityNeighbors()[i][j] == neighborCity.getName():
                    return actualCity.getCityNeighbors()[i][1]
        return -1