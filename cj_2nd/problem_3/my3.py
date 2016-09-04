import sys
import collections
from collections import defaultdict

filename = ''
if len(sys.argv) > 1:
    filename = sys.argv[1]

if filename == '':
    filename = '05.in'

testInput = open(filename, 'r')
outfile = open(filename.replace('in', 'out'), 'w')

numOfTest = int(testInput.readline().replace('\n', '').replace('\r', '').strip())

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.distances ={}

    def addNode(self, node):
        self.nodes.append(node)
        self.edges[node] = []
    
    def addEdge(self, startNode, toNode, distance):
        self.edges[startNode].append(toNode)
        self.distances[(startNode, toNode)] = distance
        
def dijsktra(graph, start, target):
    allPath = []
    visited = []
    distance = {}
    restNode = []
    path = {}

    for node in graph.nodes:
        distance[node] = sys.maxsize
        restNode.append(node)
        path[node] = []

    distance[start] = 0

    while restNode != []:
        minNode = None
        minDistance = sys.maxsize

        for node in distance:
            if distance[node] < minDistance and node not in visited:
                minDistance = distance[node]
                minNode = node
        
        restNode.remove(minNode)

        for node in graph.edges[minNode]:
            newDistance = distance[minNode] + graph.distances[(minNode, node)]
            if newDistance < distance[node]:
                path[node][:] = []
                distance[node] = newDistance
                path[node].append(minNode)
            elif newDistance == distance[node]:
                path[node].append(minNode)
        
        visited.append(minNode)

    return (path, distance)

def getMultiPath(path, start, end, past, multiPath):
    if start != end:
        past.append(end)
    else:
        past.append(start)
    for node in path[end]:
        getMultiPath(path, start, node, past, multiPath)
    if past[len(past)-1] == start:
        newPath = past[:]
        multiPath.append(newPath)
    past.pop()

def findPosition(start, end, graph):
    # print('start: ' + str(start) + ' end: ' + str(end))
    (route, distance) = dijsktra(graph, start, end)
    dist = distance[end]
    halfDistance = (float) (dist * 0.5)

    multiPath = []
    past = []
    getMultiPath(route, start, end, past, multiPath)

    meetPoints = []

    for path in multiPath:
        prevNode = None
        for node in path:
            if halfDistance > distance[node]:
                if prevNode != None and node < prevNode:
                    meetPoints.append((node, prevNode))
                else:
                    meetPoints.append((prevNode, node))
                break
            prevNode = node

    meetPoints.sort()

    return meetPoints[0]

for i in range(numOfTest):
   
    graph = Graph()
    line = testInput.readline().replace('\n', '').replace('\r', '').strip()
    ins = line.split(' ')
    numOfNode = int(ins[0])
    numOfEdge = int(ins[1])
    numOfQuery = int(ins[2])

    for i in range(numOfNode):
        graph.addNode(i+1)

    for j in range(numOfEdge):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        nodeA = int(ins[0])
        nodeB = int(ins[1])
        distance = int(ins[2])
        graph.addEdge(nodeA, nodeB, distance)
        graph.addEdge(nodeB, nodeA, distance)

    for j in range(numOfQuery):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        point = findPosition(int(ins[0]), int(ins[1]), graph)
        print(str(point[0]) + ' ' + str(point[1]))
        outfile.write(str(point[0]) + ' ' + str(point[1]) + '\n')

testInput.close()
outfile.close()