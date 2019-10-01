import TSP, City

class HillClimbing:

    def __init__(self, problem: TSP.TSP): #--> Declaracao do tipo de variavel, possível a partir do python 3
        self.myProblem=problem

    def hillClimbing(self,initialNodeName,finalNodeName,numberIterations):

        city=self.getSpecificCity(initialNodeName)
        heuristic=city.getHeuristhic()
        cost = 0

        while heuristic != 0:
            neighborCity=self.chooseNeighbor(city)
            if heuristic <= neighborCity.getHeuristhic():
                cost+=self.myProblem.distanceBetweenTwoCities(city,neighborCity)
                city=neighborCity
        return cost

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

        numberLines=len(city.getCityNeighbors())/2
        bestNeighbor = self.getSpecificCity(city.getCityNeighbors()[0][0])

        for i in range(1,numberLines):
            for j in 0 :
                neighborCity=self.getSpecificCity(city.getCityNeighbors()[i][j])
                if neighborCity.getHeuristhic() < bestNeighbor.getHeuristhic():
                    bestNeighbor =neighborCity

        return bestNeighbor