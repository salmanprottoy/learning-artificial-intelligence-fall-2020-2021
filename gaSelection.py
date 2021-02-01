import random

#chromosomes=["01101","11000","01000","10011"]

#Initialize Initial Population
def initializePopulation(chromosomes,population):

    population=[list(i) for i in chromosomes]
    bitLength=len(population[0])
    populationSize=len(population)
    
    return population,bitLength,populationSize


#Creating Decoding Scheme by Positional Value
def decodingScheme(bitLength,positionalValue):
    positionalValue=[pow(2,i) for i in range(bitLength)]
    positionalValue=positionalValue[::-1]
    return positionalValue


# decoding Chromosomes
def decode(population,populationSize,decodingScheme,bitLength,phenotype):
    for i in range(populationSize):        
        individual=population[i]
        phenotype.append(sum([int(individual[i])*decodingScheme[i] for i in range(bitLength)]))
    return phenotype

    
#computing Fitness

def computeFitness(phenotype,populationSize,fitness=[]):
    for i in range(populationSize):fitness.append(phenotype[i]*phenotype[i])
    return fitness


#Computing Individual Probability

def calculateProbability(fitness,populationSize,probability=[]):

    for i in range(populationSize):
        probability.append(round(fitness[i]/sum(fitness),2))
    return probability




#Crate Bin based on Cumulative Sum
def createBin(probability,populationSize,binned):
    
    binned.append(probability[0])
    for i in range(populationSize-1): binned.append(binned[i]+probability[i+1])     

    addValue=1-binned[-1]
    binned[-1]=binned[-1]+addValue
    return binned


#Generate Random Float Individuals
def generateRandomIndividual(populationSize,floatIndividuals=[]):

    for i in range(populationSize): floatIndividuals.append(round(random.uniform(0,1),2))

    return floatIndividuals


def returnBinIndex(ind,binn,indBinIndex,binIndex=0):
    i=binIndex
    if (ind<=binn[i]):indBinIndex=i
        
    elif (ind>binn[i]) and (ind<=binn[i+1]): indBinIndex=i+1
        
    elif (ind>binn[i+1]) and (ind<=binn[i+2]): indBinIndex=i+2
        
    elif (ind>binn[i+2]):indBinIndex=i+3

    return indBinIndex


def chosenBin(floatIndividuals,binn,chosenBinIndex=[]):

    for i in range(len(floatIndividuals)):
        ind=floatIndividuals[i]
        chosenBinIndex.append(returnBinIndex(ind,binn,indBinIndex=[]))

    return chosenBinIndex


def chosenParents(chosenBinIndex,population,parents=[]):
    for i in chosenBinIndex: parents.append(population[i])
    return parents



def selectParents(parents):
    #print(parents)
    #parent1,parent2,parent3,parent4=[],[],[],[]
    if (len(parents))==1: parent1,parent2,parent3,parent4=parents[0],parents[0],parents[0],parents[0]
    elif (len(parents))==2: parent1,parent2,parent3,parent4=parents[0],parents[1],parents[0],parents[1]
    elif (len(parents))==3: parent1,parent2,parent3,parent4=parents[0],parents[1],parents[1],parents[2]
    elif (len(parents))==4: parent1,parent2,parent3,parent4=parents[0],parents[1],parents[2],parents[3]
    else:exit

    return parent1,parent2,parent3,parent4


def selection(chromosomes,parents):

    
    population,bitLength,populationSize = initializePopulation(chromosomes,population=[])
    
    ds=decodingScheme(bitLength,positionalValue=[])
    phenotype=decode(population,populationSize,ds,bitLength,phenotype=[])
    fitness=computeFitness(phenotype,populationSize,fitness=[])
    
    probability=calculateProbability(fitness,populationSize,probability=[])
    
    binn=createBin(probability,populationSize,binned=[])
    
    floatIndividuals=generateRandomIndividual(populationSize,floatIndividuals=[])
    chosenBinIndex=chosenBin(floatIndividuals,binn,chosenBinIndex=[])        
    chosenBinIndex=list(set(chosenBinIndex))
    parent=chosenParents(chosenBinIndex,population,parents=[])

    parent1,parent2,parent3,parent4=selectParents(parent)

    parents.append(parent1)
    parents.append(parent2)
    parents.append(parent3)
    parents.append(parent4)

    avgFitness=sum(fitness)/populationSize

    return fitness,chosenBinIndex,parents


