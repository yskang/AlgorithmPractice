# 
# https://algospot.com/judge/problem/read/WHITECOLLAR
#

import sys
# import collections
# from collections import defaultdict

# rl = lambda: sys.stdin.readline().replace('\n', '').replace('\r', '').strip()
rl = lambda: input()

# testData = [
# '2',
# '4 5',
# '1 2',
# '2 1',
# '1 3',
# '3 4',
# '4 3',
# '5 6',
# '1 2',
# '1 3',
# '2 5',
# '3 4',
# '3 5',
# '4 5'    
# ]

# testData.reverse()

# rl = lambda: testData.pop()
    
numOfTestCase = int(rl())

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


for n in range(numOfTestCase):
    line = rl()
    numOfCity = int(line.split(' ')[0])
    numOfRoad = int(line.split(' ')[1])

    graph = Graph()
    for i in range(numOfCity):
        graph.addNode(i+1)

    for i in range(numOfRoad):
        line = rl()
        fromNode = int(line.split(' ')[0])
        toNode = int(line.split(' ')[1])
        graph.addEdge(fromNode, toNode, 1)

    path = dijsktra(graph, 1, numOfCity)[0]
    past = []
    multiPath = []
    getMultiPath(path, 1, numOfCity, past, multiPath)
    cities = []
    for l in multiPath:
        for city in l:
            cities.append(city)
    
    result = set(cities)
    print(" ".join(str(x) for x in result))

        
            
