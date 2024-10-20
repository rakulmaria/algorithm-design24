# Ford-Fulkerson implementation made together with Silke Bonnen for bachelors project in spring 2024
# Improvements added autumn 2024 by Silke Bonnen

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
        return f"ID: {self.id} isSource: {self.isSource} isSink: {self.isSink}\n - len(adjEdges): {len(self.adjacentEdges)}"

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
        return self._from.id, "->", self._to.id, "FLOW:", self._flow, "CAPACITY:", self._capacity

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
            print(value.printNode())

        for key, value in self.mapOfEdges.items():
            print(key.printEdge())

    def getGraphSize(self):
        return len(self.mapOfNodes)            

    def findPath(self, _from: Node, _to: Node, nodes, path=None, markedNodes=None):
        if path is None:
            path = {}
        if markedNodes is None:
            markedNodes = {}

        markedNodes[_from.id] = True

        for edge in _from.adjacentEdges:
            otherNode = edge.getOther(_from)

            if edge.residualCapacityTo(otherNode) > 0 and not markedNodes.get(
                otherNode.id
            ):
                path[otherNode.id] = edge
                markedNodes[otherNode.id] = True

                if otherNode.id == _to.id:
                    return path, True, markedNodes
                path, last_marked, markedNodes = self.findPath(
                    otherNode, _to, nodes, path, markedNodes
                )

                if last_marked:
                    return path, True, markedNodes

        return path, False, markedNodes

    def findMaxFlow(self, nodes):
        maxFlow = 0

        path, isPath, m = self.findPath(self.source, self.sink, nodes, {}, {})
        while isPath:
            bottle = 9223372036854775807
            v = self.sink

            while v.id is not self.source.id:
                v_edge = path.get(v.id)
                bottle = min(bottle, v_edge.residualCapacityTo(v))
                v = v_edge.getOther(v)

            v = self.sink
            while v.id is not self.source.id:
                v_edge = path.get(v.id)
                v_edge.addResidualFlowTo(bottle, v)
                v = v_edge.getOther(v)

            maxFlow += bottle
            path, isPath, m = self.findPath(self.source, self.sink, nodes, {}, {})
        return maxFlow
    
    def createGraph(self):
        N, M = map(int, stdin.readline().split())

        if M < (N / 2):
            print("Impossible")
            return

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

        for _ in range(M):
            A, B = map(int, stdin.readline().split())
            edge1 = Edge(self.getNode(A), self.getNode(-B))
            edge2 = Edge(self.getNode(B), self.getNode(-A))
            self.addEdge(edge1)
            self.addEdge(edge2)

        self.findMaxFlow(len(self.mapOfNodes))

        res = []
        for edge in self.mapOfEdges:
            if edge._flow > 0 and edge._from.id != 0 and edge._to.id != N + 1: 
                res.append((edge._from.id, abs(edge._to.id)))

        if len(res) != N:
            print("Impossible")
        else:
            res.sort()
            for ele in res:
                print(ele[1])

path = {}
graph = Graph()
graph.createGraph()