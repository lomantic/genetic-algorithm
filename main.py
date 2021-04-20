#!C:\Program Files\Python39\python.exe
#print("content-type: text/html; charset=utf-8\n")
# print()
import cgi
import os
import data
import func


distance = 0  # total distance of one gene
fitness = 0  # fitness of one gene
genCount = 3000  # numbers of genes generated
survivors = 300  # numbers of genes survive in one generation
generation = 50  # number of generation calculated
genes = []  # array of genes generated
survivorGenes = []  # array of genes survived in one generation
gen = []  # memory for single gen

num = 0

# generate gene and calculate fitness, distance
for j in range(genCount):
    gen = func.generateGene()
    distance = func.calDistance(gen)
    fitness = func.calFitness(distance)
    genes.append(data.Route(gen, distance, fitness))

bestGene = data.Route([0], 0, 0)
identicalCount = 0  # same result count
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
        print("PREVIOUS BEST RECORD : "+str(bestGene.fitness))
        identicalCount = 0

    if newGene.fitness > bestGene.fitness:
        bestGene = newGene
    else:

        identicalCount = identicalCount+1
    if identicalCount > breakCount:
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
