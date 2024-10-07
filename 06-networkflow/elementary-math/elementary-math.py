from sys import stdin



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

class Edge():
    def __init__(self, _from, _to, _type, _capacity=1):
        self._from = _from
        self._to = _to
        self._type = _type
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
    
    def addNodes(self, nodes):
        for node in nodes:
            if node.isSource:
                self.source = node
            if node.isSink:
                self.sink = node

            self.mapOfNodes[node.id] = node

    def getNode(self, node):
        return self.mapOfNodes.get(node.id)

    def getEdge(self, edge):
        return self.mapOfEdges.get(edge)

    def connectNodesToSink(self, nodes):
        for node in nodes:
            if self.getNode(node) == None:
                e = Edge(node, graph.getNode(sinkNode), "")
                graph.addEdges([e])
            
    def addEdges(self, edges):
        for edge in edges:

            self.mapOfEdges[edge] = edge
            # add the node from this edge and to this edge to its adjacentlist
            edge._from.addEdge(edge)
            edge._to.addEdge(edge)
        
    
    def printGraph(self):

        print(f"Nodes: {len(self.mapOfNodes)}\n")
        for key, value in self.mapOfNodes.items():
            print(f"Node ID: {key}")
            for edge in value.adjacentEdges:
                print(" - ", end="")
                edge.printEdge()

        
        print(f"\nEdges: {len(self.mapOfEdges)}\n")
        for key, value in self.mapOfEdges.items():
            if key._from == None:
                f = "None"
            else:
                f = key._from.id
            if key._to == None:
                t = "None"
            else:
                t = key._to.id
            print(f"{f} -> {t}   type: {value._type}")

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

            
    
path = {}

N = int(stdin.readline())

graph = Graph()
sourceNode = Node("source", True)
sinkNode = Node("sink", sink=True)

graph.addNodes([sourceNode, sinkNode])

graph.printGraph()

for _ in range(N):
    a, b = map(int, stdin.readline().split())

    n1 = Node((a, b))

    p = Node(a + b)
    m = Node(a - b)
    t = Node(a * b)

    graph.addNodes([n1, p, m, t])
    e0 = Edge(graph.getNode(sourceNode), graph.getNode(n1), "")

    e1 = Edge(n1, p, "+")
    e2 = Edge(n1, m, "-")
    e3 = Edge(n1, t, "*")

    graph.connectNodesToSink([p, m, t])

    graph.addEdges([e0, e1, e2, e3])


graph.printGraph()

