

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
    def __init__(self, _from, _to, _capacity = 1):
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
            value.printNode()

        for key, value in self.mapOfEdges.items():
            key.printEdge()

    def getGraphSize(self):
        return len(self.mapOfNodes)            

    def findPath(self, _from: Node, _to: Node):
        markedNodes = {}
        queue = Queue(maxsize=len(self.mapOfNodes))
        
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
        N, M = map(int, stdin.readline().split())


        source = Node(0, source=True)
        sink = Node(N + 1, sink=True)
        self.addNode(source)
        self.addNode(sink)

        for i in range(1, N+1):
            node1 = Node(i)
            node2 = Node(-i)
            self.addNode(node1)
            self.addNode(node2)
            
            # connect node to sink and source
            edge1 = Edge(self.source, node1)
            edge2 = Edge(node2, self.sink)
            self.addEdge(edge1)
            self.addEdge(edge2)

        for i in range(M):
            A, B = map(int, stdin.readline().split())
            edge1 = Edge(self.getNode(A), self.getNode(-B))
            edge2 = Edge(self.getNode(B), self.getNode(-A))
            self.addEdge(edge1)
            self.addEdge(edge2)

        self.findMaxFlow()
        self.printGraph()

        res = []
        for edge in self.mapOfEdges:
            if edge._from.id != 0 and edge._to.id != N + 1 and edge._flow > 0:
                res.append((edge._from.id, abs(edge._to.id)))


        print(len(res))
        if len(res) != N:
            print("Impossible")
        else:
            res.sort()
            for ele in res:
                print(ele[1])

path = {}
graph = Graph()
graph.createGraph()