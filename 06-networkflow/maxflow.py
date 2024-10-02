from queue import Queue

class Node():
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.adjacentEdges = []
        self.isSource = source
        self.isSink = sink

    def addEdge(self, edge):
        for e in self.adjacentEdges:
            if e.compareEdge(edge):
                return

        self.adjacentEdges.append(edge)

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
        self.listOfNodes = []
        self.listOfEdges = []
        self.source = None
        self.sink = None
    
    def addNode(self, node):
        if node.isSink:
            self.sink = node
        if node.isSource:
            self.source = node

        if node.isSink and node.isSource:
            return "Same node can't be sink and source"

        self.listOfNodes.append(node)

    def getEdge(self, edge):
        for e in self.listOfEdges:
            if edge._from == e._from and edge._to == e._to:
                return e

    def addEdge(self, edge):
        thisEdge = self.getEdge(edge)

        if thisEdge == None:
            self.listOfEdges.append(edge)
            return edge
        else:
            thisEdge._capacity += edge._capacity
            return thisEdge
    
    def getNode(self, id):
        for node in self.listOfNodes:

            if node.id == id:
                return node
    
    def printGraph(self):
        for node in self.listOfNodes:
            print("----NODE----")
            print(node.id)
            print(node.isSource)
            print(node.isSink)
            for edge in node.adjacentEdges:
                print("----OUTGOING EDGE----")
                print("From:", edge._from)
                print("To:", edge._to)


        for edge in self.listOfEdges:
            print("----EDGE----")
            print("From:", edge._from)
            print("To:", edge._to)
            print("Capacity:", edge._capacity)
            print("Flow:", edge._flow)
            

    def findPath(self, _from: Node, _to: Node):
        markedNodes = {}
        queue = Queue(maxsize=nodes)

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

            
    

nodes, edges, source, sink = input().split()

nodes = int(nodes)
edges = int(edges)
source = int(source)
sink = int(sink)

graph = Graph()


for node in range(nodes):
    if node == source:
        graph.addNode(Node(node, source=True))
    elif node == sink:
        graph.addNode(Node(node, sink=True))
    else:
        graph.addNode(Node(node))
    

for ele in range(edges):
    _from, _to, _capacity = input().split()
    _capacity = int(_capacity)
    _from = int(_from)
    _to = int(_to)

    newEdge = Edge(graph.getNode(_from), graph.getNode(_to), _capacity)
    # newEdge.setResidualEdge()

    updatedEdge = graph.addEdge(newEdge)

    graph.getNode(_from).addEdge(updatedEdge)
    graph.getNode(_to).addEdge(updatedEdge)
    

path = {}

#print("The path is:", graph.findPath(graph.source, graph.sink))

#for edge in path.values():
#    edge.printEdge()


maxFlow = graph.findMaxFlow()

numberOfEdges = 0
stringList = []

for edge in graph.listOfEdges:
    if edge._flow > 0:
        numberOfEdges += 1
        result = str(edge._from.id) + " " + str(edge._to.id) + " " + str(edge._flow)
        stringList.append(result)

stringList.sort()
print(nodes, maxFlow, numberOfEdges)
for ele in stringList:
    print(ele)


