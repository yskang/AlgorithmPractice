import sys
import collections
from collections import defaultdict

filename = ''
if len(sys.argv) > 1:
    filename = sys.argv[1]

if filename == '':
    filename = 'testInput.in'

testInput = open(filename, 'r')

numOfTest = int(testInput.readline().replace('\n', '').replace('\r', '').strip())

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

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
    halfDist = dist/2
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
    return resultString

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
        resultA = findPosition(int(ins[0]), int(ins[1]), graph)
        resultB = findPosition(int(ins[1]), int(ins[0]), graph)
        if resultA != resultB:
            [a1, a2] = resultA.split(' ')
            [b1, b2] = resultB.split(' ')
            a1 = int(a1)
            a2 = int(a2)
            b1 = int(b1)
            b2 = int(b2)
            if a1 < b1:
                print(resultA)
            elif a1 > b1:
                print(resultB)
            else:
                if a2 < b2:
                    print(resultA)
                else:
                    print(resultB)
        else:
            print(resultA)

testInput.close()