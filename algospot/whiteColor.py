# 
# https://algospot.com/judge/problem/read/WHITECOLLAR
#

import sys
import collections
from collections import defaultdict

# rl = lambda: sys.stdin.readline()

testData = [
'2',
'4 5',
'1 2',
'2 1',
'1 3',
'3 4',
'4 3',
'5 6',
'1 2',
'1 3',
'2 5',
'3 4',
'3 5',
'4 5'    
]

testData.reverse()

rl = lambda: testData.pop()
    
numOfTestCase = int(rl())

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.removed = {}
    
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge_oneWay(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def add_edge_twoWay(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance        
    
    def removeEdgeTwoWay(self, from_node, to_node):
        self.removed[(from_node, to_node)] = self.distances[(from_node, to_node)]
        self.removed[(to_node, from_node)] = self.distances[(to_node, from_node)]  
        self.distances[(from_node, to_node)] = 999999
        self.distances[(to_node, from_node)] = 999999

    def removeEdgeOneWay(self, from_node, to_node):
        self.removed[(from_node, to_node)] = self.distances[(from_node, to_node)]
        self.distances[(from_node, to_node)] = 999999

    def recover(self):
        for edge in self.removed.keys():
            self.distances[edge] = self.removed[edge]
        self.removed = {}

def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes: 
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

for n in range(numOfTestCase):
    line = rl()
    numOfCity = int(line.split(' ')[0])
    numOfRoad = int(line.split(' ')[1])

    graph = Graph()
    for i in range(numOfCity):
        graph.add_node(i+1)

    for i in range(numOfRoad):
        line = rl()
        fromNode = int(line.split(' ')[0])
        toNode = int(line.split(' ')[1])
        graph.add_edge_oneWay(fromNode, toNode, 1)

    (visited, path) = dijsktra(graph, 1)

    results = []
    results.append(numOfCity)

    while True:
        while True:
            last = path[results[len(results)-1]]
            results.append(last)
            if last == 1:
                break

    r = set(results.sort())
    print(results)
