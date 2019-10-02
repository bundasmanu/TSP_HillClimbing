from typing import List
import City
import TSP
import HillClimbing

def createCity(name : str, cityNeighbors, heuristic : int):
    return City.City(name=name,neighbors=cityNeighbors, heuristhic=heuristic)

def configureValues():

    cityNames=['A','B','C','D']
    heuristicValues=[5,3,2,0]

    cityANeighbors=[['b',2],['c',1]]
    cityBNeighbors = [['c', 3], ['d', 5]]
    cityCNeighbors = [['b', 3], ['d', 5]]

    return cityNames,heuristicValues,cityANeighbors,cityBNeighbors,cityCNeighbors

def main():

    '''
        Definicao inicial de um vetor de heuristicas
        Definicao das matrizes [vizinhos] [distancia]--> uma para cada cidade
        Definicao de um vetor com os nomes das cidades
    '''
    cityNames,heuristicValues,cityANeighbors,cityBNeighbors,cityCNeighbors= configureValues()

    cityArray=[]
    counter=0

    for i in range(4):
        counter=0
        city= None
        if i == 0:
            city=createCity(cityNames[i],cityANeighbors,heuristicValues[i])
        elif i==1:
            city=createCity(cityNames[i], cityBNeighbors, heuristicValues[i])
        elif i==2:
            city=createCity(cityNames[i], cityCNeighbors, heuristicValues[i])
        elif i==3:
            city=createCity(cityNames[i], [], heuristicValues[i])
        else:
            counter=1

        if counter==0:
            cityArray.append(city)

    for i in range(4):
        print(cityArray[i])

    '''
    Criacao do meu objeto TSP--> representante do problema em questao, agregando as cidades existentes 
    '''

if __name__ == "__main__":
    main()