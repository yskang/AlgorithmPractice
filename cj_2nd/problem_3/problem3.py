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
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.removed = {}
    
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
    
    def removeEdge(self, from_node, to_node):
        self.removed[(from_node, to_node)] = self.distances[(from_node, to_node)]
        self.removed[(to_node, from_node)] = self.distances[(to_node, from_node)]  
        self.distances[(from_node, to_node)] = 999999
        self.distances[(to_node, from_node)] = 999999

    def recover(self):
        for edge in self.removed.keys():
            self.distances[edge] = self.removed[edge]
        self.removed = {}

def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes: 
        # min_node = None
        # for node in nodes:
        #     if node in visited:
        #         if min_node is None:
        #             min_node = node
        #         elif visited[node] < visited[min_node]:
        #             min_node = node

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

def findPosition(start, end, graph):
    # print('start: ' + str(start) + ' end: ' + str(end))
    (distance, route) = dijsktra(graph, start)
    dist = distance[end]
    halfDist = dist * 0.5
    # print('distance: ' + str(dist))
    # print(end)
    nextNode = end
    while True:
        prevNode = nextNode
        nextNode = route[nextNode]
        if distance[nextNode] < halfDist:
            a = prevNode
            b = nextNode
            if a < b: 
                resultString = str(a) + ' ' + str(b)
            else:
                resultString = str(b) + ' ' + str(a)
            break
        elif distance[nextNode] == halfDist:
            a = prevNode
            b = nextNode
            resultString = str(b) + ' ' + str(b)
            break          
        # print(nextNode)
    # print("------------")
    return (resultString, dist)

for i in range(numOfTest):
   
    graph = Graph()
    line = testInput.readline().replace('\n', '').replace('\r', '').strip()
    ins = line.split(' ')
    numOfNode = int(ins[0])
    numOfEdge = int(ins[1])
    numOfQuery = int(ins[2])

    for i in range(numOfNode):
        graph.add_node(i+1)

    for j in range(numOfEdge):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        nodeA = int(ins[0])
        nodeB = int(ins[1])
        distance = int(ins[2])
        graph.add_edge(nodeA, nodeB, distance)
        # graph.add_edge(nodeB, nodeA, distance)

    for j in range(numOfQuery):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        resultStrings = []
        resultPairs = []
        (result, dist) = findPosition(int(ins[0]), int(ins[1]), graph)

        resultStrings.append(result)
        o = result.split(' ')
        pair = (int(o[0]), int(o[1]))
        resultPairs.append(pair)
            
        distance = dist

        res = resultStrings[0].split(' ')
        graph.removeEdge(int(res[0]), int(res[1]))

        while True:
            if res[0] == res[1]:
                break
    
            (result, dist) = findPosition(int(ins[0]), int(ins[1]), graph)

            if dist <= distance:
                resultStrings.append(result)
                o = result.split(' ')
                pair = (int(o[0]), int(o[1]))
                resultPairs.append(pair)

                if o[0] != o[1]:
                    break
                graph.removeEdge(int(o[0]), int(o[1]))

            else:
                break

        resultPairs.sort()
        print(resultPairs)
        outfile.write(str(resultPairs[0][0]) + ' ' + str(resultPairs[0][1]) + '\n')

        graph.recover()


testInput.close()