# Ford-Fulkerson implementation made together with Silke Bonnen for bachelors project in spring 2024
from collections import defaultdict
import time
import math
from queue import Queue
from sys import stdin

def primeFactors(n):
    i = 2
    factors = set()
    # Divide out all 2s first
    while n % i == 0:
        factors.add(i)
        n //= i
    
    i = 3
    # Now check odd numbers
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
    # If n is a prime number larger than 2, add it to the factors
    if n > 1:
        factors.add(n)
    return factors


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
        curMin = 74852374924
        curMax = 1

        for i in range(N):
            n = int(stdin.readline())
            if n < curMin:
                curMin = n
            if n > curMax:
                curMax = n
            nodes.append(n)

        for id in nodes:
            sink = False
            source = False
            if id == curMin:
                source = True
            if id == curMax:
                sink = True

            node = Node(id, source=source, sink=sink)
            self.addNode(node)

        primes = defaultdict(list)

        for id in nodes:
            prime_factors_set = primeFactors(id)
            for p in prime_factors_set:
                primes[p].append(id)



        # create the edges
        for prime, group in primes.items():
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    n1 = self.getNode(group[i])
                    n2 = self.getNode(group[j])
                    #weight = math.gcd(n1.id, n2.id)
                    #weight = math.gcd(n1.id, n2.id)  # This will be prime `p`, so no need to recalculate
                    if prime > 1:
                        edge1 = Edge(n1, n2, prime)
                        edge2 = Edge(n2, n1, prime)
                        self.addEdge(edge1)
                        self.addEdge(edge2)
                        
        #print(self.findMaxFlow())




start_time = time.time()     
path = {}        
graph = Graph()
graph.createGraph()
print("--- %s seconds ---" % (time.time() - start_time))