#!C:\Program Files\Python39\python.exe
# print("content-type: text/html; charset=utf-8\n")
# print()
import cgi
import os
import func
import csv


# read TSP.csv and store it to list
cities = []
with open('TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    i = 0
    for row in reader:
        cities.append(row)
    '''  if i > 50:
            break
        i = i+1'''

    func.sendToFunc(cities)


distance = 0  # total distance of one gene
fitness = 0  # fitness of one gene
genCount = 2000  # numbers of genes generated
survivors = 1000  # numbers of genes survive in one generation
generation = 1000000  # generation span approximate inf
genes = []  # array of genes generated
survivorGenes = []  # array of genes survived in one generation
gen = []  # memory for single gen

num = 0

'''
# generate gene and calculate fitness, distance
for j in range(genCount):
    gen = func.generateGene()
    distance = func.calDistance(gen)
    fitness = func.calFitness(distance)
    genes.append(func.TSP(gen, distance, fitness))
'''
# TSP.csv type version
for j in range(genCount):
    gen = func.generateGene(len(cities))
    distance = func.calDistance(gen)
    fitness = func.calFitness(distance)
    genes.append(func.geneInfo(gen, distance, fitness))


bestGene = func.geneInfo([0], 0, 0)
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
        print("PREVIOUS BEST RECORD : "+str(bestGene.length))
        identicalCount = 0
    else:
        identicalCount = identicalCount+1
        print("identical count : "+str(identicalCount))
    if newGene.fitness > bestGene.fitness:
        bestGene = newGene
        recordGuardCount = 0
    else:
        recordGuardCount = recordGuardCount+1
        print("Record Guard Count : "+str(recordGuardCount))

    if identicalCount > breakCount or recordGuardCount > breakCount*2:
        break


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
