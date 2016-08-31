import sys

filename = sys.argv[1]

test_input = open(filename, 'r')

numberOfTest = int(test_input.readline().replace('\n', '').replace('\r', '').strip())

nodesR = []
distanceR = []
nodesC = []
distanceC = []
branchPoint = 0

def initData():
    nodesR[:] = []
    distanceR[:] = []
    nodesC[:] = []
    distanceC[:] = []
    branchPoint = 0

def getCostA():
    cost = 0
    currentCost = nodesR[0]
    for i in range(branchPoint - 1):
        if currentCost > nodesR[i]:
            currentCost = nodesR[i]
        cost = cost + currentCost * distanceR[i]
    return (cost, currentCost)

def getCostB(initCost):
    cost = 0
    currentCost = initCost
    for i in range(branchPoint - 1, len(nodesR)):
        if currentCost > nodesR[i]:
            currentCost = nodesR[i]
        cost = cost + currentCost * distanceR[i]
    return cost

def getForwardCost(initCost, returnPoint):
    cost = 0
    currentCost = initCost
    for i in range(returnPoint):
        if currentCost > nodesC[i]:
            currentCost = nodesC[i]
        cost = cost + currentCost * distanceC[i]
    return (cost, currentCost)

def getBackwardCost(initCost, returnPoint):
    cost = 0
    currentCost = initCost
    for i in range(returnPoint, 0, -1):
        if currentCost > nodesC[i]:
            currentCost = nodesC[i]
        cost = cost + currentCost * distanceC[i - 1]
    return (cost, currentCost)

def getBranchCost(initCost, returnPoint):
    (forwardCost, lastCost) = getForwardCost(initCost, returnPoint)
    (backwardCost, lastCost) = getBackwardCost(lastCost, returnPoint)
    return (forwardCost + backwardCost, lastCost)

def checkCost():
    (costA, lastCost) = getCostA()
    costB = getCostB(lastCost)

    totalCosts = []
    totalCosts.append(costA + costB)

    for i in range(len(nodesC)):
        if lastCost > nodesC[i]:
            (branchCost, branchLastCost) = getBranchCost(lastCost, i)
            costB = getCostB(branchLastCost)
            totalCosts.append(costA + branchCost + costB)

    # print(min(totalCosts))
    output.write(str(min(totalCosts)) + '\n')

output = open(filename.replace('in', 'out'), 'w')

for i in range(numberOfTest):
    initData()
    numNodeRow = int(test_input.readline().replace('\n', '').replace('\r', '').strip())
    line = test_input.readline().replace('\n', '').replace('\r', '').strip()
    ins = line.split(' ')
    for j in range(0, 2 * (numNodeRow - 1), 2):
        nodesR.append(int(ins[j]))
        distanceR.append(int(ins[j+1]))
    ins = test_input.readline().replace('\n', '').replace('\r', '').strip().split(' ')
    branchPoint = int(ins[0])
    numNodeCol = int(ins[1])
    line = test_input.readline().replace('\n', '').replace('\r', '').strip()
    ins = line.split(' ')
    for j in range(0, 2 * numNodeCol, 2):
        distanceC.append(int(ins[j]))
        nodesC.append(int(ins[j+1]))

    if branchPoint-1 >= len(nodesR):
        nodesC.insert(0, 100)
    else:
        nodesC.insert(0, nodesR[branchPoint-1])
    
    checkCost()

test_input.close()
output.close()