# my own dijsktra implementation.
import sys

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


graph = Graph()

for i in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.addNode(i)

graph.addEdge('A', 'B', 1)
graph.addEdge('A', 'C', 2)
graph.addEdge('A', 'D', 2)
graph.addEdge('A', 'E', 2)
graph.addEdge('B', 'C', 1)
graph.addEdge('C', 'F', 1)
graph.addEdge('D', 'F', 1)
graph.addEdge('E', 'F', 1)

path = []
path = dijsktra(graph, 'A', 'F')[0]
past = []
multipath = []
getMultiPath(path, 'A', 'F', past, multipath)
print('end')
print(multipath)


