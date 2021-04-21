import data
import random
import operator
import numpy as np
import csv
# not organized with class

# New function with identical name for TSP.csv

'''
class Route:
    def __init__(self, order, length, fitness):
        self.order = order
        self.length = length
        self.fitness = fitness

    def testPrint(self):
        print("order : "+str(self.order))
        print("length : "+str(self.length))
        print("fitness : "+str(self.fitness))
'''


class geneInfo:
    def __init__(self, order, length, fitness):
        self.order = order
        self.length = length
        self.fitness = fitness

    def testPrint(self):
        print("order : "+str(self.order))
        print("length : "+str(self.length))
        print("fitness : "+str(self.fitness))


def generateGene(geneElementCount):
    # 1~999 cuz TSP starts from city '0'
    citys = [i for i in range(1, geneElementCount)]
    random.shuffle(citys)
    return citys


def calDistance(list):  # input : list containing 1~999
    # print("list[0] : "+str(list[0]))  ##### test code######
    # travel city'0'~ city'list[0]'
    distance = getDistance(0, list[0])
    ##print("distance: "+str(distance))
    for i in range(len(list)-2):  # idx=0~998  len(list)==999
        distance = distance + getDistance(list[i], list[i+1])
    distance = distance + getDistance(list[len(list)-1], 0)
    return distance


def getDistance(former, latter):
    #print("getDis activate") ######test code########
    #print("former : "+str(former))
    #print("latter : "+str(latter))
    city1 = [float(cities[former][0]), float(cities[former][1])]
    city2 = [float(cities[latter][0]), float(cities[latter][1])]
    dist = np.linalg.norm(np.array(city1)-np.array(city2))
    # print(dist)  ####### test code######3
    return dist


def sendToFunc(cityList):
    global cities
    cities = cityList


'''
def generateGene():  # TSP complete
    citys = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    random.shuffle(citys)
    return citys


def calDistance(list):  # TSP complete
    distance = data.distance_A[list[0]]
    for i in range(len(list)-1):
        distance = distance + getDistance(list[i], list[i+1])
    distance = distance + getDistance(list[len(list)-1], "A")
    return distance


def getDistance(former, latter):  # TSP complete
    if former == "A":
        return data.distance_A[latter]
    elif former == "B":
        return data.distance_B[latter]
    elif former == "C":
        return data.distance_C[latter]
    elif former == "D":
        return data.distance_D[latter]
    elif former == "E":
        return data.distance_E[latter]
    elif former == "F":
        return data.distance_F[latter]
    elif former == "G":
        return data.distance_G[latter]
    elif former == "H":
        return data.distance_H[latter]
    elif former == "I":
        return data.distance_I[latter]
    elif former == "J":
        return data.distance_J[latter]
    elif former == "K":
        return data.distance_K[latter]

'''


def calFitness(distance):
    fitness = (1000000/distance)**2
    return fitness


def topFitness(genes, superiorCount):
    superiorGenes = []
    genes.sort(key=operator.attrgetter('length'))
    superiorGenes = genes[:superiorCount]  # most superior genes
    # del genes[:superiorCount] # delete genes already selected

    return superiorGenes


def wheelRoulette(genes):
    max = sum(gene.fitness for gene in genes)
    pick = random.uniform(0, max)
    current = 0
    for gene in genes:
        current += gene.fitness
        if current > pick:
            return gene


def sortGene(genes, geneCount):
    #superiorCount = 10
    i = 0
    # candidates=topFitness(genes,superiorCount)
    candidates = []
    while i < geneCount:
        # if use superior genes-superiorCount
        sortedGene = wheelRoulette(genes)
        if i == 0:
            candidates.append(sortedGene)
        elif overlapKiller(candidates, sortedGene):
            candidates.append(sortedGene)
        else:
            i = i-1  # if overlap : resort gene

        i = i+1

    return candidates


def overlapKiller(candidates, newcomer):
    for gene in candidates:
        if gene == newcomer:
            #print("overlap detected")
            return False
    return True


def crossover(parent):
    turn = random.randint(0, 1)  # choose whose gene is base
    # number of genes inherit to child from base
    # select base gene where to cut and inherit by random
    geneNum = random.randint(1, len(cities)-2)

    if turn == 0:
        child = mixGene(parent[0], parent[1], geneNum)  # base dad
    else:
        child = mixGene(parent[1], parent[0], geneNum)  # base mom

    return child


def mixGene(baseGene, sourceGene, geneNum):
    #pickedGene= random.sample(baseGene.order,geneNum)
    # pickedGene.sort()  #unproper for TSP
    mutationRate = 20  # 1/mutationRate
    #newGene = data.Route([0], 0, 0)
    newGene = geneInfo([0], 0, 0)
    base = baseGene.order[:geneNum]
    source = sourceGene.order[:]
    source = sourceGeneInspector(source, base)
    newGene.order = base+source

    if 1 == random.randint(1, mutationRate):  # mutation
        newGene.order = mutation(newGene.order)

    newGene.length = calDistance(newGene.order)
    newGene.fitness = calFitness(newGene.length)

    return newGene


def sourceGeneInspector(sourceGene, pickedGene):
    # print("source: "+str(sourceGene)) # test code error fix
    #print("picked: "+str(pickedGene))
    for i in range(len(pickedGene)):
        sourceGene.remove(pickedGene[i])
    return sourceGene


def mutation(gene):
    mutationLevel = random.randint(len(gene)//2, len(gene))
    for i in range(mutationLevel):
        exchange = random.sample(range(0, 5), 2)
        gene[exchange[0]], gene[exchange[1]
                                ] = gene[exchange[1]], gene[exchange[0]]
    return gene


def newGeneration(geneList, geneCount):
    geneCount = geneCount - len(geneList)
    newGenerationList = []
    for i in range(geneCount):
        parent = sortGene(geneList, 2)
        child = crossover(parent)
        newGenerationList.append(child)
    newGenerationList = newGenerationList+geneList
    return newGenerationList


def getBestGene(gene):
    bestGene = gene[0]
    for i in range(len(gene)-2):
        if gene[i].fitness < gene[i+1].fitness:
            bestGene = gene[i+1]
    return bestGene
