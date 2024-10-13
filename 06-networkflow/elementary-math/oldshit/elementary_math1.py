# Ford-Fulkerson implementation made together with Silke Bonnen for bachelors project in spring 2024
# Using DFS

from sys import stdin

class Node():
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.adjacentEdges = {}
        self.isSource = source
        self.isSink = sink

    def addEdge(self, edge):
        print(f"adding edge {edge.printEdge()} to N: {self.id}")
        if edge not in self.adjacentEdges.values():
            self.adjacentEdges[edge] = edge 

class Edge():
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to
        self._capacity = 1
        self._flow = 0

    def increaseCapacity(self):
        self._capacity += 1

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
        return str(self._from.id) + " -> " + str(self._to.id) + " FLOW: " + str(self._flow) + " CAPACITY: " + str(self._capacity)


class Graph():
    def __init__(self):
        self.mapOfNodes = {}
        self.mapOfEdges = {}
        self.source = None
        self.sink = None
        self.maxFlow = 0

    def addNode(self, node):
        if node.isSource:
            self.source = node
        if node.isSink:
            self.sink = node

        self.mapOfNodes[node.id] = node

    def getNode(self, node):
        return self.mapOfNodes.get(node.id)
    
    def addEdge(self, edge):
        thisEdge = self.getEdge(edge)

        if thisEdge is None:
            print(f"edge {edge.printEdge()} doesn't exist - adding it")
            a = self.getNode(edge._from) 
            b = self.getNode(edge._to)
            
            if a != None and b != None:
                self.mapOfEdges.update({(a, b): edge})

            self.mapOfEdges.update({(edge._from.id, edge._to.id): edge})
            # and add the edge to the adjacency list
            edge._from.addEdge(self.getEdge(edge))
            edge._to.addEdge(self.getEdge(edge))
        else:
            print(f"edge already exists - increasing the capacity")
            thisEdge._capacity += edge._capacity

    def getEdge(self, edge):
        return self.mapOfEdges.get((edge._from.id, edge._to.id))
    
    def connectNodesToSink(self, nodes):
        for node in nodes:
            if self.mapOfEdges.get((node.id, self.sink.id)) == None:
                e = Edge(node, graph.getNode(self.sink))
                self.addEdge(e)
    
    def printGraph(self):

        print(f"Nodes: {len(self.mapOfNodes)}\n")
        for key, value in self.mapOfNodes.items():
            print(f"Node ID: {key}")

            for edge in value.adjacentEdges:
                print(" - ", end="")
                print(edge.printEdge())

        
        print(f"\nEdges: {len(self.mapOfEdges)}\n")
        for key, value in self.mapOfEdges.items():
            print(f"{key[0]} -> {key[1]}   C: {value._capacity}, F: {value._flow}")

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
            print(f"{_from.id} -> {otherNode.id}")
            print(f"rest capacity: {edge.residualCapacityTo(otherNode)}")
            

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
            print("--- looking for new path ---")
            for edge in path.keys():
                print(f"key: {edge}")
                path[edge].printEdge()


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

            print(f"bottle: {bottle}")

            maxFlow += bottle

            path, isPath, m = self.findPath(self.source, self.sink, nodes, {}, {})
        return maxFlow

    def result(self):
        filteredEdges = []

        for edge in self.mapOfEdges.values():
            if edge._from.id != "source" and edge._to.id != "sink" and edge._flow > 0:
                filteredEdges.append(edge)

        result = []
        for edge in filteredEdges:
            result.append(self.getBinaryOperator(edge._from.id, edge._to.id))

        if len(result) < N:
            print("impossible")
        else:
            for ele in result:
                print(ele)

    def getBinaryOperator(self, n1, n2):
        if n1[0] - n1[1] == n2:
            return str(f"{n1[0]} - {n1[1]} = {n2}")
        elif n1[0] + n1[1] == n2:
            return str(f"{n1[0]} + {n1[1]} = {n2}")
        else:
            return str(f"{n1[0]} * {n1[1]} = {n2}")

    

path = {}

N = int(stdin.readline())

graph = Graph()
sourceNode = Node("source", True)
sinkNode = Node("sink", sink=True)

graph.addNode(sourceNode)
graph.addNode(sinkNode)

for _ in range(N):
    a, b = map(int, stdin.readline().split())

    n1 = Node((a, b))

    print(f"n1: {n1.id}")

    p = Node(a + b)
    m = Node(a - b)
    t = Node(a * b)
    print(f"plus: {p.id}")
    print(f"minus: {m.id}")
    print(f"times: {t.id}")
    # why does node 1 not have adjacent edges, how do I create them

    graph.addNode(n1)
    graph.addNode(p)
    graph.addNode(m)
    graph.addNode(t)
    e0 = Edge(graph.getNode(sourceNode), graph.getNode(n1))

    e1 = Edge(n1, p)
    e2 = Edge(n1, m)
    e3 = Edge(n1, t)

    graph.connectNodesToSink([p, m, t])

    graph.addEdge(e0)
    graph.addEdge(e1)
    graph.addEdge(e2)
    graph.addEdge(e3)



print(graph.findMaxFlow(len(graph.mapOfNodes)))
print("---")
graph.printGraph()
print("---")
graph.result()