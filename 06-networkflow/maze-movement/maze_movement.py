# Ford-Fulkerson implementation made together with Silke Bonnen for bachelors project in spring 2024
from collections import defaultdict
import time
import math
from queue import Queue
from sys import stdin

class Node():
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.adjacentEdges = {}
        self.isSource = source
        self.isSink = sink

    def addEdge(self, edge):
       if edge not in self.adjacentEdges.values():
            self.adjacentEdges[edge] = edge 

    def printNode(self):
        print(f"ID: {self.id} isSource: {self.isSource} isSink: {self.isSink}")

class Edge():
    def __init__(self, _from, _to, _capacity):
        self._from = _from
        self._to = _to
        self._capacity = _capacity
        self._flow = 0
        
    def residualCapacityTo(self, node):
        if node.id is self._to.id:
            value = self._capacity - self._flow
        else:
            value = self._flow
        return value

    def addResidualFlowTo(self, flowValue, node):
        if node.id is self._to.id:
            self._flow += flowValue
        else:
            self._flow -= flowValue
    
    def getOther(self, node: Node):
        if node.id is self._from.id:
            return self._to
        else:
            return self._from
    
    def compareEdge(self, edge):
        if self._from is edge._from and self._to is edge._to and self._capacity is edge._capacity:
            return True
        else:
            return False
        
    def printEdge(self):
        print(self._from.id, "->", self._to.id, "FLOW:", self._flow, "CAPACITY:", self._capacity)

class Graph():
    def __init__(self):
        self.mapOfNodes = {}
        self.mapOfEdges = {}
        self.source = None
        self.sink = None
    
    def addNode(self, node):
        if node.isSource:
            self.source = node
        if node.isSink:
            self.sink = node
        self.mapOfNodes[node.id] = node

    def getNode(self, id):
        return self.mapOfNodes.get(id)

    def getEdge(self, edge):
        return self.mapOfEdges.get(edge)

    def addEdge(self, edge):
        self.mapOfEdges[edge] = edge
        # add the node from this edge and to this edge to its adjacentlist
        edge._from.addEdge(edge)
        edge._to.addEdge(edge)
        
    
    def printGraph(self):
        for key, value in self.mapOfNodes.items():
            print(f"Key: {key}, Value: {value.printNode()}")

        for key, value in self.mapOfEdges.items():
            key.printEdge()

    def getGraphSize(self):
        return len(self.mapOfNodes)
            

    def findPath(self, _from: Node, _to: Node):
        markedNodes = {}
        queue = Queue(maxsize=graph.getGraphSize())
        
        markedNodes[_from.id] = True 

        queue.put(item=_from)             # and put it on the queue

        while not queue.empty():
            currentNode = queue.get()
            
            for edge in currentNode.adjacentEdges:
                print("---")
                otherNode = edge.getOther(currentNode)

                if edge.residualCapacityTo(otherNode) > 0 and not markedNodes.get(otherNode.id):
                    path[otherNode.id] = edge
                    markedNodes[otherNode.id] = True 
                    queue.put(otherNode)
            
        
        return markedNodes.get(_to.id)


    def findMaxFlow(self):
        maxFlow = 0
        global path

        while(self.findPath(self.source, self.sink)):
            bottle = 9223372036854775807
            v = self.sink

            while v.id is not self.source.id:
                bottle = min(bottle, path.get(v.id).residualCapacityTo(v))
                v = path.get(v.id).getOther(v)

            v = self.sink
            while v.id is not self.source.id:
                path.get(v.id).addResidualFlowTo(bottle, v)
                v = path.get(v.id).getOther(v)

            
            maxFlow += bottle

            path = {}
        
        return maxFlow
    
    def createGraph(self):
        N = int(stdin.readline())

        nodes = []
        dict = {}
        curMin = 74852374924578
        curMax = 1

        for i in range(N):
            n = int(stdin.readline())
            if n < curMin:
                curMin = n
            if n > curMax:
                curMax = n
            nodes.append(n)
            dict[n] = i

        # create the edges
        for i in range(len(nodes)):
            n = nodes[i]
            n1 = Node(n, source=n==curMin, sink=n==curMax)
            self.addNode(n1)
            for j in range(i+1, len(nodes)):
                m = nodes[j]
                n2 = Node(m, source=m==curMin, sink=m==curMax)
                self.addNode(n2)
                weight = math.gcd(n, m)
                if weight > 1:
                    edge1 = Edge(n1, n2, weight)
                    edge2 = Edge(n2, n1, weight)
                    self.addEdge(edge1)
                    self.addEdge(edge2)
                        
        print(self.findMaxFlow())
        self.printGraph()

start_time = time.time()     
path = {}        
graph = Graph()
graph.createGraph()
print("--- %s seconds ---" % (time.time() - start_time))