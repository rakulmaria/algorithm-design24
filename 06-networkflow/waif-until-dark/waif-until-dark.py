# Ford-Fulkerson implementation made together with Silke Bonnen for bachelors project in spring 2024

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
        i = 0
        for key, value in self.mapOfNodes.items():
            print(f"i: {i} Key: {key}, Value: {value}")
            i += 1

        i = 0
        for key, value in self.mapOfEdges.items():
            if key._from == None:
                f = "None"
            else:
                f = key._from.id
            if key._to == None:
                t = "None"
            else:
                t = key._to.id
            print(f"i: {i} - {f} -> {t} - {value}")
            i += 1

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
children, toys, categories = map(int, stdin.readline().split())

graph = Graph()
source = Node("s", source=True)
sink = Node("t", sink=True)

graph.addNode(source)
graph.addNode(sink)

# add all the toy nodes
for toy in range(1, toys+1):
    n = Node(toy)
    graph.addNode(n)


# add all the child nodes and connect them to the toy they prefer to play with
# child's id start at toys + 1
for child in range(toys+1, toys+children+1):
    line = stdin.readline().split()
    
    n = Node(child)
    # we want to connect this node to the source node
    inital_edge = Edge(source, n, 1)

    graph.addNode(n)
    graph.addEdge(inital_edge)

    # we want to connect this node to each of its toys
    for i in range(1, int(line[0]) + 1):
        e = Edge(n, graph.getNode(int(line[i])), 1) # TODO: what should capacity be?
        graph.addEdge(e)

toyInCategory = {}

# now check if there are any categories that we need to take care of
for category in range(categories):
    line = stdin.readline().split()
    
    # how many toys are a part of this category
    incoming_edges = line[0]
    # how many toys max can be played with of this category
    outgoing_edges = int(line[len(line)-1])

    # the id's of the toys in this category
    toys_in_category = line[1:(len(line)-1)]

    n = Node("c" + str(category))
    graph.addNode(n)

    # then add the incoming edges to the category node
    for toy in toys_in_category:
        e = Edge(graph.getNode(int(toy)), n, 1) # TODO: capacity?    
        graph.addEdge(e)
        toyInCategory[int(toy)] = int(toy)
        
    # add the outgoing edges to the category node
    for i in range(outgoing_edges):
        e = Edge(graph.getNode(n.id), sink, 1)    
        graph.addEdge(e)

# now add the toys that are not within the categories
for toy in range(1, toys+1):
    if toy not in toyInCategory.values():
        e = Edge(graph.getNode(toy), sink, 1)
        graph.addEdge(e)


# --- now we have our graph - time to solve max flow in it
print(graph.findMaxFlow())
