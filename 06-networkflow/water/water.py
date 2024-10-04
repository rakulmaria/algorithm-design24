
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

    def updateCapacity(self, newCapacity):
        self._capacity += newCapacity

    def getCapacity(self):
        return self._capacity
    
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

    def addEdge(self, edge):
        self.mapOfEdges[(edge._from.id, edge._to.id)] = edge
        # add the node from this edge and to this edge to its adjacentlist
        edge._from.addEdge(edge)
        edge._to.addEdge(edge)

    def getEdge(self, f, t):
        return self.mapOfEdges.get((f, t))
    
    def printGraph(self):
        i = 0
        print("NODES")
        for key, value in self.mapOfNodes.items():
            print(f"( {value.id} )")
            for edge in value.adjacentEdges:
                edge.printEdge()
            i += 1

        i = 0
        print("EDGES")
        for key, value in self.mapOfEdges.items():
            print(f"{key[0]} -> {key[1]} CAP: {value.getCapacity()}")
            i += 1

    def getGraphSize(self):
        return len(self.mapOfNodes)
            

    def findPath(self, _from: Node, _to: Node):
        markedNodes = {}
        queue = Queue(maxsize=self.getGraphSize())
        
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

    def find_path_BFS(self, source, sink):
        marked_vertices = {}
        queue = Queue(maxsize=self.getGraphSize())
        path = {}

        marked_vertices[source.id] = True
        queue.put(source)

        while not queue.empty() and not marked_vertices.get(sink.id):
            current_vertex = queue.get()

            for edge in current_vertex.adjacent_edges:
                other_vertex = edge.get_other_vertex(current_vertex)

                if edge.get_residual_capacity_to(
                    other_vertex
                ) > 0 and not marked_vertices.get(other_vertex.id):
                    path[other_vertex.id] = edge
                    marked_vertices[other_vertex.id] = True
                    queue.put(other_vertex)

        if marked_vertices.get(sink.id):
            return path
        else:
            return None

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
            e1 = Edge(graph.getNode(f), graph.getNode(t), c)
            e2 = Edge(graph.getNode(t), graph.getNode(f), c)
            graph.addEdge(e1)
            graph.addEdge(e2)

        maxflow = graph.findMaxFlow()
        print(maxflow)

        # add the improvements
        for _ in range(improvements):
            f, t, c = map(int, stdin.readline().split())
            
            e1 = graph.getEdge(f, t)
            e2 = graph.getEdge(t, f)
            # if the edge doesn't exist, add it
            if e1 == None:
                e1 = Edge(graph.getNode(f), graph.getNode(t), c)
                e2 = Edge(graph.getNode(t), graph.getNode(f), c)
                graph.addEdge(e1)
                graph.addEdge(e2)
            # else update it 
            else:
                e1.updateCapacity(c)
                e2.updateCapacity(c)
            maxflow += graph.findMaxFlow()
            print(maxflow)

path = {}
solve()