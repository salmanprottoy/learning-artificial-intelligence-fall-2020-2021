import random
from gaSelection import initializePopulation,decodingScheme,decode,computeFitness,selection

def crossOver(bitLength,selectedParents,offSprings=[]):

    crossoverPoint=random.choice(list(range(1,bitLength-1,1)))
    #print(crossoverPoint)
    offSprings.append(selectedParents[0][:crossoverPoint]+selectedParents[1][crossoverPoint:])
    offSprings.append(selectedParents[1][:crossoverPoint]+selectedParents[0][crossoverPoint:])

    crossoverPoint=random.choice(list(range(1,bitLength-1,1)))
    #print(crossoverPoint)
    offSprings.append(selectedParents[2][:crossoverPoint]+selectedParents[3][crossoverPoint:])
    offSprings.append(selectedParents[3][:crossoverPoint]+selectedParents[2][crossoverPoint:])
    
    return offSprings

def makeChromosomes(offSpring):
    chromosome=""
    for i in offSpring: chromosome += i
    newChromosomes.append(chromosome)

    return newChromosomes

def findBestIndex(parentsFitness,offspringsFitness):

    maxPKeys,maxOffKeys=[],[]

    pFitnessDict={i:parentsFitness[i] for i in range(len(parentsFitness))}
    offFitnessDict={i:offspringsFitness[i] for i in range(len(offspringsFitness))}
    
    #print(pFitnessDict,offFitnessDict)
    
    pFitnessValues=list(pFitnessDict.values())
    maxP=max(pFitnessValues)    
    maxPkey=[key for (key,value) in pFitnessDict.items() if value==maxP]
    maxPKeys.append(maxPkey[0])

    pFitnessDict.pop(maxPkey[0])

    pFitnessValues=list(pFitnessDict.values())
    maxP=max(pFitnessValues)    
    maxPkey=[key for (key,value) in pFitnessDict.items() if value==maxP]
    maxPKeys.append(maxPkey[0])

    # Returning Two Max Offspring Keys
    
    offFitnessValues=list(offFitnessDict.values())
    maxOff=max(offFitnessValues)    
    maxOffkey=[key for (key,value) in offFitnessDict.items() if value==maxOff]
    maxOffKeys.append(maxOffkey[0])

    offFitnessDict.pop(maxOffkey[0])

    offFitnessValues=list(offFitnessDict.values())
    maxOff=max(offFitnessValues)    
    maxOffkey=[key for (key,value) in offFitnessDict.items() if value==maxOff]
    maxOffKeys.append(maxOffkey[0])
    
    return maxPKeys,maxOffKeys

def calculateFitness(newChromosomes):
    population,bitLength,populationSize = initializePopulation(newChromosomes,population=[])
    ds=decodingScheme(bitLength,positionalValue=[])
    phenotype=decode(population,populationSize,ds,bitLength,phenotype=[])
    fitness=computeFitness(phenotype,populationSize,fitness=[])

    return fitness



chromosomes=["01101","11000","01000","10011"]

generation=1
avgFitness=0
selectedParents=[]
newChromosomes=[]

    
while avgFitness<961:



    bitLength=len(chromosomes[0])

    fitness,chosenBinIndex,selectedParents=selection(chromosomes,selectedParents)
    avgFitness=sum(fitness)/len(fitness)
    
    parentsFitness=fitness

    print("Generation ",generation," Average Fitness: ",avgFitness)


    offSprings=[]
    offSprings=crossOver(bitLength,selectedParents)
    for i in offSprings: makeChromosomes(i)


    fitness=calculateFitness(newChromosomes)    
    offspringsFitness=fitness
      
    maxPKeys,maxOffKeys=findBestIndex(parentsFitness,offspringsFitness)

    newGenPopulation=[]


    newGenPopulation.append(chromosomes[maxPKeys[0]])
    newGenPopulation.append(chromosomes[maxPKeys[1]])
    newGenPopulation.append(newChromosomes[maxOffKeys[0]])
    newGenPopulation.append(newChromosomes[maxOffKeys[1]])

    chromosomes=newGenPopulation
    print(chromosomes)

    
    
    
    generation=generation+1


