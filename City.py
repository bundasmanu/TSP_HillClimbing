from typing import List

class City:

    def __init__(self,name,neighbors: List[str][int],heuristhic  : int):

        '''

        :param name: Nome da Cidade
        :param neighbors: Array descrevendo os nomes dos vizinhos, e a distancia para os mesmos, array Bidimensional
            --> Cidade A:
                        [ B 2 ] cOLUNA 1 -->Vizinho e Coluna 2--> Distancia
                        [ C 1 ]
                        [ D 7 ]
        :param heuristhic: valor da sua heuristica
        '''
        self.cityName=name
        self.cityNeighbors=neighbors
        self.heuristhic=heuristhic

    def getName(self):
        return self.cityName

    def setName(self,newCityName):
        self.cityName=newCityName

    def getCityNeighbors(self):
        return self.cityNeighbors

    def setCityNeighbors(self,newCityNeighboars):
        self.cityNeighbors=newCityNeighboars

    def getHeuristhic(self):
        return self.heuristhic

    def setNewHeuristhic(self,newHeuristhicValue):
        self.heuristhic=newHeuristhicValue

    def __str__(self):
        return "\nCity Name: "+self.cityName+"\tHeuristhic: "+self.heuristhic+"\tNeighbors: "+self.cityNeighbors