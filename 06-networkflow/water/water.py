
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

    def updateCapacity(self, newCapacity):
        self._capacity += newCapacity

    def getCapacity(self):
        return self._capacity

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

    def addEdge(self, edge):
        self.mapOfEdges[(edge._from.id, edge._to.id)] = edge
        # add the node from this edge and to this edge to its adjacentlist
        edge._from.addEdge(edge)
        edge._to.addEdge(edge)

    def getEdge(self, f, t):
        return self.mapOfEdges.get((f, t))
        
    def getMinCut(self):
        source = self.source
        sink = self.sink

        source_cap = 0
        for e in source.adjacentEdges.values():
            cap = e.getCapacity()
            source_cap += cap

        sink_cap = 0
        for e in sink.adjacentEdges.values():
            cap = e.getCapacity()
            sink_cap += cap

        return min(source_cap, sink_cap)
    
def solve():
    while True:
        try:
            line = stdin.readline()
            if line == "":
                break
        except:
            break

        stations, initial_pipes, improvements = map(int, line.split())
        graph = Graph()

        # add the source and sink nodes, which are always labeled as 1 and 2
        source_node = Node(1, True)
        sink_node = Node(2, sink=True)

        graph.addNode(source_node)
        graph.addNode(sink_node)

        # add next nodes from 3 .. stations + 1
        for node in range(3, stations+1):
            n = Node(node)
            graph.addNode(n)

        # connect the nodes with the initial pipes
        for edge in range(initial_pipes):
            f, t, c = map(int, stdin.readline().split())
            e = Edge(graph.getNode(f), graph.getNode(t), c)
            graph.addEdge(e)

        print(graph.getMinCut())

        # add the improvements
        for _ in range(improvements):
            f, t, c = map(int, stdin.readline().split())
            
            e = graph.getEdge(f, t)
            # if the edge doesn't exist, add it
            if e == None:
                e = Edge(graph.getNode(f), graph.getNode(t), c)
                graph.addEdge(e)
            # else update it 
            else:
                e.updateCapacity(c)
            print(graph.getMinCut())

solve()