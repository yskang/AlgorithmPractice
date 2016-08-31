import sys

filename = ''
if len(sys.argv) > 1:
    filename = sys.argv[1]

if filename == '':
    filename = 'set3.in'

testInput = open(filename, 'r')
testOutput = open(filename.replace('in', 'out'), 'w')

numOfTest = int(testInput.readline().replace('\n', '').replace('\r', '').strip())

def distance(point, center):
    delta = complex(*point) - complex(*center)
    deltaLen = abs(delta)
    return deltaLen

def isClockwise(center, target, top, right, bottom, left):
    if center[0] < target[0]:
        if center[1] < target[1]:
            if target[0] <= top[0] and center[1] >= left[1]:
                return True
            else:
                return False
        elif center[1] > target[1]:
            if center[0] >= top[0] and target[1] >= right[1]:
                return True
            else:
                return False 
        else:
            if target[1] == top[1]:
                return True
            else:
                return False 
    elif center[0] > target[0]:
        if center[1] < target[1]:
            if center[0] <= bottom[0] and target[1] <= left[1]:
                return True
            else:
                return False 
        elif center[1] > target[1]:
            if target[0] >= bottom[0] and center[1] <= right[1]:
                return True
            else:
                return False
        else:
            if target[1] == bottom[1]:
                return True
            else:
                return False  
    else:
        if center[1] > target[1]:
            if center[0] == right[0]:
                return True
            else:
                return False
        elif center[1] < target[1]:
            if center[0] == left[0]:
                return True
            else:
                return False            
        else:
            return False

def calcMinLengthCircle(points):
    minX = 99999
    minY = 99999
    maxX = -99999
    maxY = -99999

    topPoint = None
    leftPoint = None
    rightPoint = None
    bottomPoint = None

    for (x, y) in points:
        if x < minX:
            minX = x
            leftPoint = (x, y)
        if x > maxX:
            maxX = x
            rightPoint = (x, y)
        if y < minY:
            minY = y
            bottomPoint = (x, y)
        if y > maxY:
            maxY = y
            topPoint = (x, y)

    sortedPoints = []
    pointA = points[0]
    points.remove(pointA)
    sortedPoints.append(pointA)

    while True:
        if len(points) == 1:
            sortedPoints.append(points[0])
            break

        minDistance = 99999
        closePoint = None

        for point in points:
            dist = distance(point, pointA)
            if dist < minDistance and isClockwise(pointA, point, topPoint, rightPoint, bottomPoint, leftPoint):
                minDistance = dist
                closePoint = point
        
        sortedPoints.append(closePoint)
        points.remove(closePoint)
        pointA = closePoint
    
    # out1 = open('out1.txt', 'w')
    # for p in sortedPoints:
    #     out1.write(str(p[0]) + str(' ') + str(p[1]) + "\n")
    # out1.close()

    lengths = []

    for k in range(len(sortedPoints)):
        backupPoint = sortedPoints[k]
        del sortedPoints[k]

        lenOut = 0

        for i in range(0, len(sortedPoints)-1):
            lenOut = lenOut + distance(sortedPoints[i], sortedPoints[i+1])
        lenOut = lenOut + distance(sortedPoints[len(sortedPoints)-1], sortedPoints[0])

        sortedPoints.insert(k, backupPoint)

        lengths.append(lenOut)

    return min(lengths)


def isOutOfBound(target, pointS, pointE):
    if target == pointS or target == pointE:
        return False

    if pointS[0] == pointE[0]:
        if pointS[1] > pointE[1]:
            if target[0] < pointS[0]:
                return True
            else:
                return False
        else:
            if target[0] > pointS[0]:
                return True
            else:
                return False

    if pointS[1] == pointE[1]:
        if pointS[0] > pointE[0]:
            if target[1] < pointS[1]:
                return False
            else:
                return True
        else:
            if target[1] > pointS[1]:
                return False
            else:
                return True

    delta = (pointS[1] - pointE[1]) / (pointS[0] - pointE[0])
    alpha = pointS[1] - delta * pointS[0]
    result = delta * target[0] + alpha - target[1]

    if pointS[0] > pointE[0]: 
        if result > 0:
            return False
        elif result == 0:
            return False
        else:
            return True
    else:
        if result < 0:
            return False
        elif result == 0:
            return False
        else:
            return True        

def getOuters(points):
    if len(points) <= 1:
        return 0
    elif len(points) == 2:
        return 2 * distance(points[0], points[1])
    elif len(points) == 3:
        return distance(points[0], points[1]) + distance(points[1], points[2]) + distance(points[2], points[0])

    minX = 99999
    minY = 99999
    maxX = -99999
    maxY = -99999

    topPoint = None
    leftPoint = None
    rightPoint = None
    bottomPoint = None

    for (x, y) in points:
        if x < minX:
            minX = x
            leftPoint = (x, y)
        if x > maxX:
            maxX = x
            rightPoint = (x, y)
        if y < minY:
            minY = y
            bottomPoint = (x, y)
        if y > maxY:
            maxY = y
            topPoint = (x, y)

    outers = []
    outers.append(topPoint)

    startPoint = topPoint
    points.remove(startPoint)
    secondPoint = points[0]
    points.append(startPoint)

    while True:
        outPoint = None

        for point in points:
            if isOutOfBound(point, startPoint, secondPoint):
                outPoint = point
                break

        if outPoint != None:
            secondPoint = outPoint
        else:
            if secondPoint == topPoint:
                break
            startPoint = secondPoint
            outers.append(secondPoint)
            points.remove(secondPoint)
            secondPoint = points[0]
    
    return outers


def getBoundLength(points):
    if len(points) <= 1:
        return 0
    elif len(points) == 2:
        return 2 * distance(points[0], points[1])
    elif len(points) == 3:
        return distance(points[0], points[1]) + distance(points[1], points[2]) + distance(points[2], points[0])

    minX = 99999
    minY = 99999
    maxX = -99999
    maxY = -99999

    topPoint = None
    leftPoint = None
    rightPoint = None
    bottomPoint = None

    for (x, y) in points:
        if x < minX:
            minX = x
            leftPoint = (x, y)
        if x > maxX:
            maxX = x
            rightPoint = (x, y)
        if y < minY:
            minY = y
            bottomPoint = (x, y)
        if y > maxY:
            maxY = y
            topPoint = (x, y)

    outers = []
    outers.append(topPoint)

    startPoint = topPoint
    points.remove(startPoint)
    secondPoint = points[0]
    points.append(startPoint)

    while True:
        outPoint = None

        for point in points:
            if isOutOfBound(point, startPoint, secondPoint):
                outPoint = point
                break

        if outPoint != None:
            secondPoint = outPoint
        else:
            if secondPoint == topPoint:
                break
            startPoint = secondPoint
            outers.append(secondPoint)
            points.remove(secondPoint)
            secondPoint = points[0]
    
    lenOut = 0

    for i in range(0, len(outers)-1):
        lenOut = lenOut + distance(outers[i], outers[i+1])
    lenOut = lenOut + distance(outers[len(outers)-1], outers[0])

    return lenOut

def getSubset(mySet, index, setA):
    if index == len(mySet):
        setA.append(mySet)
        return
    getSubset(mySet[:], index + 1, setA)
    mySet.pop(index)
    getSubset(mySet[:], index, setA)

def calcMinLengthSmallSet(points):
    setA = []
    getSubset(points, 0, setA)            

    lengthList = []

    for i in range(int(len(setA) / 2)):
        lenA = getBoundLength(setA[i])
        lenB = getBoundLength(setA[len(setA)-i-1])
        lengthList.append(lenA + lenB)

    return min(lengthList)

def calcMinLengthBigSet(points):
    lengthList = []

    localPoints = []

    for point in points:
        localPoints.append(point)
    
    outers = []
    outers = getOuters(localPoints)

    for outer in outers:
        localPoints[:] = []
        for point in points:
            localPoints.append(point)

        localPoints.remove(outer)
        lengthBound = getBoundLength(localPoints)
        lengthList.append(lengthBound)
    
    for i in range(len(outers)-1):
        localPoints[:] = []
        for point in points:
            localPoints.append(point)

        twoPointLen = 2 * distance(outers[i], outers[i+1])
        localPoints.remove(outers[i])
        localPoints.remove(outers[i+1])
        lengthBound = getBoundLength(localPoints)
        lengthList.append(lengthBound + twoPointLen)

    localPoints[:] = []
    for point in points:
        localPoints.append(point)

    twoPointLen = 2 * distance(outers[len(outers)-1], outers[0])
    localPoints.remove(outers[len(outers)-1])
    localPoints.remove(outers[0])
    lengthBound = getBoundLength(localPoints)
    lengthList.append(lengthBound + twoPointLen)
    
    return min(lengthList)    


def isCircle(points):
    for (x, y) in points:
        if x < 1000 or y < 1000:
            return False
    return True

def calcMinLength(points):
    result = ''
    if len(points) < 100:
        result = calcMinLengthSmallSet(points)
    elif isCircle(points):
        result = calcMinLengthCircle(points)
    else:
        result = calcMinLengthBigSet(points)
    return result


for i in range(numOfTest):
    numOfPoints = int(testInput.readline().replace('\n', '').replace('\r', '').strip())
    print(numOfPoints)
    points = []
    for j in range(numOfPoints):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        point = (int(ins[0]), int(ins[1]))
        points.append(point)
    
    if len(sys.argv) > 1:
        testOutput.write(str("%0.5f\n" %calcMinLength(points)))
    else:
        print("%0.5f" %calcMinLength(points))
