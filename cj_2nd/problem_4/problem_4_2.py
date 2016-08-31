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

def calcMinLength(points):
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


for i in range(numOfTest):
    numOfPoints = int(testInput.readline().replace('\n', '').replace('\r', '').strip())
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
