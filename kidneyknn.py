
a=[]

wbcc=input('Enter wbcc=')
a.append(wbcc)
htn=input('Enter htn=')
a.append(htn)
rbc=input('Enter rbc=')
a.append(rbc)
sod=input('Enter sod=')
a.append(sod)
ba=input('Enter ba=')
a.append(ba)
su=input('Enter su=')
a.append(su)
bu=input('Enter bu=')
a.append(bu)
hemo=input('Enter hemo=')
a.append(hemo)
ane=input('Enter ane=')
a.append(ane)

print(a)

def convert(s1):
    new1 = ""
    for x1 in s1:
        new1 += x1
    return new1
s2 = (a)
print(convert(s2))
testdata1 = (",".join(s2))
print(testdata1)
a=[]
txt = open('testingchronic.csv', 'a')
txt.write('\n'+testdata1)


import csv
import math
import operator

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    # prepare data
    trainingSet = []
    testSet = []
    with open('chronickidneyknns.csv', 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

        for x in range(len(dataset) - 1):
            for y in range(9):
                dataset[x][y] = float(dataset[x][y])
            trainingSet.append(dataset[x])





    with open('testingchronic.csv', 'r') as csvfile1:
        lines1 = csv.reader(csvfile1)
        print(lines1)
        dataset1 = list(lines1)
        print(dataset1)
        for p in range(len(dataset1)):
            for q in range(9):
                dataset[p][q] = float(dataset[p][q])
            testSet.append(dataset1[p])

    print("trainingset",trainingSet)
    print("testingset",testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    # generate predictions
    predictions = []
    k = 3
    for x in range(len(testSet)):
        #print("len",len(testSet))
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

    import matplotlib.pyplot as plt;
    x = [0, 1, 2]
    y = [accuracy, 0, 0]
    plt.bar(x, y)
    plt.show()
main()