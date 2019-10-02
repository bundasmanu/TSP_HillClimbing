import TSP, City

class HillClimbing:

    def __init__(self, problem: TSP.TSP): #--> Declaracao do tipo de variavel, possível a partir do python 3
        self.myProblem=problem

    def hillClimbing(self,initialNodeName):

        city=self.getSpecificCity(initialNodeName)
        heuristic=city.getHeuristhic()
        cost = 0
        route=[city.getName()]

        while heuristic != 0:
            neighborCity=self.chooseNeighbor(city)
            if heuristic >= neighborCity.getHeuristhic():
                cost+=self.myProblem.distanceBetweenTwoCities(city,neighborCity)
                heuristic=neighborCity.getHeuristhic()
                route.append(neighborCity.getName())
                city=neighborCity
            else: # --> Caso nao entre no if, fica pendurado naquela cidade, e para evitar loop infinito retorna logo
                return cost,route
        return cost,route

    def getSpecificCity(self, nodeName):

        for i in range(len(self.myProblem.getCities())):
            if self.myProblem.getCities()[i].getName() == nodeName:
                return self.myProblem.getCities()[i]

        return None

    def chooseNeighbor(self, city : City.City):

        '''

        :param city: Cidade em avaliacao
        :return: -->Retorno do vizinho que apresenta melhor qualidade de todos
        '''

        numberLines=len(city.getCityNeighbors())
        bestNeighbor = self.getSpecificCity(city.getCityNeighbors()[0][0])

        for i in range(1,(numberLines)):
            for j in range(1) : #--> So conta o 0
                neighborCity=self.getSpecificCity(city.getCityNeighbors()[i][j])
                if neighborCity.getHeuristhic() < bestNeighbor.getHeuristhic():
                    bestNeighbor =neighborCity

        return bestNeighbor