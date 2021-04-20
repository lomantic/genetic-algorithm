import data,random,operator
# not organized with class

def generateGene():
    citys = ["B","C","D","E","F","G","H","I","J","K"]
    random.shuffle(citys)
    return citys

def calDistance(list):
    distance = data.distance_A[list[0]]
    for i in range(len(list)-1):
        distance = distance+ getDistance(list[i],list[i+1])
    distance= distance+ getDistance(list[len(list)-1],"A")
    return distance


def getDistance(former,latter):
    if former=="A":
        return data.distance_A[latter]
    elif former=="B":
        return data.distance_B[latter]
    elif former=="C":
        return data.distance_C[latter]
    elif former=="D":
        return data.distance_D[latter]
    elif former=="E":
        return data.distance_E[latter]
    elif former=="F":
        return data.distance_F[latter]
    elif former=="G":
        return data.distance_G[latter]
    elif former=="H":
        return data.distance_H[latter]
    elif former=="I":
        return data.distance_I[latter]
    elif former=="J":
        return data.distance_J[latter]
    elif former=="K":
        return data.distance_K[latter]

def calFitness(distance):
    fitness = (10000/distance)**2
    return fitness

def topFitness(genes,superiorCount):
    superiorGenes=[]
    genes.sort(key=operator.attrgetter('length'))
    superiorGenes=genes[:superiorCount] # most superior genes
    #del genes[:superiorCount] # delete genes already selected

    return superiorGenes


def wheelRoulette(genes):
    max = sum(gene.fitness for gene in genes)
    pick = random.uniform(0, max)
    current = 0
    for gene in genes:
        current += gene.fitness
        if current > pick:
            return gene

def sortGene(genes,geneCount):
    #superiorCount = 10
    i=0
    #candidates=topFitness(genes,superiorCount)
    candidates=[]
    while i<geneCount:
        sortedGene=wheelRoulette(genes) # if use superior genes-superiorCount
        if i==0:
            candidates.append(sortedGene)
        elif overlapKiller(candidates,sortedGene):
            candidates.append(sortedGene)
        else:
            i=i-1 #if overlap : resort gene

        i=i+1

    return candidates

def overlapKiller(candidates,newcomer):
    for gene in candidates:
        if gene==newcomer:
            #print("overlap detected")
            return False
    return True

def crossover(parent):
    turn=random.randint(0,1) # choose whose gene is base
    geneNum = random.randint(1,5) # number of genes inherit to child from base

    if turn ==0:
        child= mixGene(parent[0],parent[1],geneNum) # base dad
    else:
        child= mixGene(parent[1],parent[0],geneNum) # base mom

    return child

def mixGene(baseGene,sourceGene,geneNum):
    #pickedGene= random.sample(baseGene.order,geneNum)
    #pickedGene.sort()  #unproper for TSP
    mutationRate =20 # 1/mutationRate
    newGene= data.Route([0],0,0)
    base= baseGene.order[:geneNum]
    source=sourceGene.order[:]
    source= sourceGeneInspector(source,base)
    newGene.order= base+source

    if 1==random.randint(1,mutationRate): #mutation
        newGene.order= mutation(newGene.order)

    newGene.length = calDistance(newGene.order)
    newGene.fitness= calFitness(newGene.length)

    return newGene


def sourceGeneInspector(sourceGene,pickedGene):
    #print("source: "+str(sourceGene)) # test code error fix
    #print("picked: "+str(pickedGene))
    for i in range(len(pickedGene)):
        sourceGene.remove(pickedGene[i])
    return sourceGene

def mutation(gene):
    mutationLevel=random.randint(len(gene)//2,len(gene))
    for i in range(mutationLevel):
        exchange= random.sample(range(0, 5), 2)
        gene[exchange[0]],gene[exchange[1]]=gene[exchange[1]],gene[exchange[0]]
    return gene

def newGeneration(geneList,geneCount):
    geneCount= geneCount - len(geneList)
    newGenerationList=[]
    for i in range(geneCount):
        parent = sortGene(geneList,2)
        child = crossover(parent)
        newGenerationList.append(child)
    newGenerationList= newGenerationList+geneList
    return newGenerationList

def getBestGene(gene):
    bestGene= gene[0]
    for i in range(len(gene)-2):
        if gene[i].fitness<gene[i+1].fitness:
            bestGene=gene[i+1]
    return bestGene
