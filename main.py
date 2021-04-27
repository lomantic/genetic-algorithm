#!C:\Program Files\Python39\python.exe
# print("content-type: text/html; charset=utf-8\n")
# print()
import cgi
import os
import func
import csv
import sys


# read TSP.csv and store it to list
cities = []
distancePerCity = []
nearbyCity = []
print("Reading TSP.csv ...")
with open('TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    # i = 0
    for row in reader:
        cities.append(row)
    '''  if i > 50:
            break
        i = i+1'''
print("TSP.csv Read complete")

print("Reading totalDistance.csv ...")
with open('totalDistance.csv', mode='r', newline='') as allDistance:
    reader = csv.reader(allDistance)
    for row in reader:
        distancePerCity.append(row)
print("totalDistance.csv Read complete")

print("Reading cityDistance.csv ...")
with open('cityDistance.csv', mode='r', newline='') as cityDistance:
    reader = csv.reader(cityDistance)
    for row in reader:
        nearbyCity.append(row)
print("cityDistance.csv Read complete")

tuple(cities)
tuple(distancePerCity)
tuple(nearbyCity)
func.sendCityList(cities)
func.sendTotalDistanceList(distancePerCity)
func.sendNearbyCityList(nearbyCity)


gen = []  # city travel order for single gen
distance = 0.0  # total distance of single gene
fitness = 0.0  # fitness of single gene
genCount = 400  # number of genes per generation
survivors = 200  # number of genes survived in single generation
generation = 1000000  # generation span approximate inf
genes = []  # list of genes generated
survivorGenes = []  # array of genes survived in one generation


'''
# generate gene and calculate fitness, distance
for j in range(genCount):
    gen = func.generateGene()
    distance = func.calDistance(gen)
    fitness = func.calFitness(distance)
    genes.append(func.TSP(gen, distance, fitness))
'''
# TSP.csv type version
print("creating 1st Gen ...")
for j in range(genCount):
    gen = func.generateGene(len(cities))
    distance = func.calDistance(gen)
    # fitness = func.calFitness(distance) # inproper fitness calculation
    genes.append(func.geneInfo(gen, distance, fitness))
    # fitness: yet calculated

# calculate fitness
func.calFitness(genes)

bestGene = func.geneInfo([0], 999999, 0)
identicalCount = 0  # same result count
recordGuardCount = 0  # best record guard count
breakCount = 9  # forbid infinity loop
newRecord = 0
bestRecord = 0  # prevent excessive mutaion
for j in range(generation):
    # sort genes with wheelRoulette : count survivors
    survivorGenes = func.sortGene(genes, survivors)
    # create new generation
    genes = func.newGeneration(survivorGenes, genCount)
    newGene = func.getBestGene(genes)
    newRecord = newGene.fitness
    # Test print code
    if newGene.length != bestGene.length:
        print("================ "+str(j+1) +
              "th Gen ===========================")
        newGene.testPrint()
        if j > 0:  # do not print at 1st gen
            print("PREVIOUS BEST RECORD : "+str(bestGene.length))
        identicalCount = 0
    else:
        identicalCount = identicalCount+1
        print("identical count : "+str(identicalCount))

    if newGene.length < bestGene.length:
        bestGene = newGene
        recordGuardCount = 0
    else:
        recordGuardCount = recordGuardCount+1
        print("Record Guard Count : "+str(recordGuardCount))

    if identicalCount > breakCount or recordGuardCount > breakCount*2:
        break
    print("\ncreating next gen...\n")


print("===================Final Gen=====================")
bestGene.testPrint()
if identicalCount > breakCount:
    print("BREAK : best result identical over " + str(identicalCount)+" times")

'''
    bestGene.append(CandidateGene)

    result=func.getBestGene(bestGene)
    result.testPrint()
'''


''' #survivor test code
print("SURVIVORS")
for gene in survivorGenes:
    gene.testPrint()
'''
