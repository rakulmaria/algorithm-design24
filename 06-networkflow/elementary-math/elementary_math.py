# Ford-Fulkerson implementation made together with Silke Bonnen for bachelors project in spring 2024
# Improvements added autumn 2024 by Silke Bonnen

from sys import stdin

class Node():
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.source = source
        self.sink = sink
        self.adjacentEdges = {}

    def getEdge(self, edge):
        return self.adjacentEdges.get(edge)

    def addEdge(self, edge):
        self.adjacentEdges[edge] = edge


class Edge():
    def __init__(self, _from, to):
        self._from = _from
        self.to = to
        self.capacity = 1
        self.flow = 0
    
    def increaseCapacity(self):
        self.capacity += 1

    def residualCapacityTo(self, node):
        if node.id is self.to.id:
            value = self.capacity - self.flow
        else:
            value = self.flow
        return value
    
    def addResidualFlowTo(self, value, node):
        if node.id is self.to.id:
            self.flow += value
        else:
            self.flow -= value

    def getOther(self, node):
        if node.id is self._from.id:
            return self.to
        else:
            return self._from
        
    def compareEdge(self, edge):
        if (self._from is edge._from and self.to is edge.to and self.capacity is edge.capacity):
            return True
        else:
            return False

    def printEdge(self):
        return self._from.id, "->", self.to.id, "FLOW:", self.flow, "CAPACITY:", self.capacity


class Graph():
    def __init__(self):
        self.mapOfNodes = {}
        self.mapOfEdges = {}
        self.source = None
        self.sink = None

    def addNode(self, node):
        if node.source:
            self.source = node
        if node.sink:
            self.sink = node
        if self.getNode(node) is None:
            self.mapOfNodes.update({node.id: node})

    def getNode(self, node):
        return self.mapOfNodes.get(node.id)
    
    def addEdge(self, edge):
        thisEdge = self.getEdge(edge)

        if thisEdge is None:
            self.mapOfEdges.update({(edge._from.id, edge.to.id): edge})
        else:
            thisEdge.increaseCapacity()

        self.getNode(edge._from).addEdge(self.getEdge(edge))
        self.getNode(edge.to).addEdge(self.getEdge(edge))

    def getEdge(self, edge):
        return self.mapOfEdges.get((edge._from.id, edge.to.id))
    
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
        N = int(stdin.readline())

        # create the source and sink node
        source = Node(id="source", source=True)
        sink = Node(id="sink", sink=True)
        self.addNode(source)
        self.addNode(sink)

        calculationNodes = set()

        for _ in range(N):
            a, b = map(int, stdin.readline().split())

            n = Node((a, b))
            e = Edge(self.source, n)
            self.addNode(n)        
            self.addEdge(e)    

            plus = Node(a + b)
            minus = Node(a - b)
            times = Node(a * b)

            self.addNode(plus)
            self.addNode(minus)
            self.addNode(times)

            e1 = Edge(self.getNode(n), self.getNode(plus))
            e2 = Edge(self.getNode(n), self.getNode(minus))
            e3 = Edge(self.getNode(n), self.getNode(times))

            self.addEdge(e1)
            self.addEdge(e2)
            self.addEdge(e3)
            calculationNodes.add(plus.id)
            calculationNodes.add(minus.id)
            calculationNodes.add(times.id)

        # connect calculationNodes to sink
        for node in calculationNodes:
            e = Edge(self.mapOfNodes.get(node), self.sink)
            self.addEdge(e)

        self.findMaxFlow(len(self.mapOfNodes))

        result = []

        for edge in self.mapOfEdges.values():
            if edge._from.id != "source" and edge.to.id != "sink" and edge.flow > 0:
                a, b = edge._from.id
                res = edge.to.id

                if a + b == res:
                    result.append(f"{a} + {b} = {res}")
                elif a - b == res:
                    result.append(f"{a} - {b} = {res}")
                elif a * b == res:
                    result.append(f"{a} * {b} = {res}")

        if len(result) != N:
            print("impossible")
        else:
            print(*result, sep="\n")

        


            
            
            

graph = Graph()

graph.createGraph()

