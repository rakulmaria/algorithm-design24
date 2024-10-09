from sys import stdin
import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, id, source=False, sink=False, a=None, b=None, res=None):
        self.id = id
        self.adjacentEdges = set()
        self.isSource = source
        self.isSink = sink
        self.a = a
        self.b = b
        self.res = res

    def addEdge(self, edge):
        self.adjacentEdges.add(edge)

    def printNode(self):
        print("----NODE----")
        print(f"node id: {self.id}")
        print(f"a: {self.a}, b: {self.b}, res: {self.res}")
        print(f"is source: {self.isSource}")
        print(f"is sink: {self.isSink}")


class Edge:
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
        if (
            self._from is edge._from
            and self._to is edge._to
            and self._capacity is edge._capacity
        ):
            return True
        else:
            return False


class Graph:
    def __init__(self):
        self.dictOfNodes = {}
        self.resToNodes = {}
        self.dictOfEdges = {}
        self.source = None
        self.sink = None

    def addNode(self, node: Node):
        if node.isSink:
            self.sink = node
        if node.isSource:
            self.source = node

        if node.isSink and node.isSource:
            return "Same node can't be sink and source"

        self.dictOfNodes.update({node.id: node})

        if node.res is not None:
            self.resToNodes.update({node.res: node})

    def getEdge(self, edge: Edge):
        return self.dictOfEdges.get((edge._from.id, edge._to.id))

    def addEdge(self, edge: Edge):
        thisEdge = self.getEdge(edge)

        if thisEdge is None:
            self.dictOfEdges.update({(edge._from.id, edge._to.id): edge})
            return edge
        else:
            thisEdge._capacity += edge._capacity
            return thisEdge

    def getNode(self, id, res=False):
        if res:
            return self.resToNodes.get(id)
        return self.dictOfNodes.get(id)

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

    def printGraph(self):
        for node in self.dictOfNodes.values():
            node.printNode()

        for edge in self.dictOfEdges.values():
            print("----EDGE----")
            print("From:")
            edge._from.printNode()
            print("To:")
            edge._to.printNode()
            print("Capacity:", edge._capacity)
            print("Flow:", edge._flow)


def create_graph():
    n = int(stdin.readline())
    nodes = 2
    graph = Graph()

    graph.addNode(Node(-2, source=True))
    graph.addNode(Node(-1, sink=True))

    j = 0

    for i in range(n):
        a, b = stdin.readline().split()
        a = int(a)
        b = int(b)
        graph.addNode(Node(j, a=a, b=b))
        ab_node_id = j
        nodes += 1

        newEdge = Edge(graph.getNode(-2), graph.getNode(j), 1)
        updatedEdge = graph.addEdge(newEdge)
        graph.getNode(-2).addEdge(updatedEdge)
        graph.getNode(j).addEdge(updatedEdge)
        j += 1

        # plus
        j, nodes = add_node_and_edge(a + b, graph, j, ab_node_id, nodes)

        # minus
        j, nodes = add_node_and_edge(a - b, graph, j, ab_node_id, nodes)

        # mul
        j, nodes = add_node_and_edge(a * b, graph, j, ab_node_id, nodes)

    return nodes, graph, n


def add_node_and_edge(res, graph, j, ab_node_id, nodes):
    res_node = graph.getNode(res, True)
    res_node_id = -2222

    if res_node is None:
        graph.addNode(Node(j, res=res))
        res_node_id = j
        j += 1
        nodes += 1
        newEdge = Edge(graph.getNode(res_node_id), graph.getNode(-1), 1)
        updatedEdge = graph.addEdge(newEdge)
        graph.getNode(-1).addEdge(updatedEdge)
        graph.getNode(res_node_id).addEdge(updatedEdge)
    else:
        res_node_id = res_node.id
    if graph.dictOfEdges.get((ab_node_id, res_node_id)) is None:
        newEdge = Edge(graph.getNode(ab_node_id), graph.getNode(res_node_id), 1)
        updatedEdge = graph.addEdge(newEdge)
        graph.getNode(ab_node_id).addEdge(updatedEdge)
        graph.getNode(res_node_id).addEdge(updatedEdge)

    return j, nodes


def solve():
    nodes, graph, equations = create_graph()

    maxFlow = graph.findMaxFlow(nodes)

    if maxFlow < equations:
        print("impossible")
    else:
        for edge in graph.dictOfEdges.values():
            if edge._flow > 0 and edge._from.id >= 0 and edge._to.id >= 0:
                a = edge._from.a
                b = edge._from.b
                res = edge._to.res

                if a + b == res:
                    print(f"{edge._from.a} + {edge._from.b} = {edge._to.res}")
                elif a - b == res:
                    print(f"{edge._from.a} - {edge._from.b} = {edge._to.res}")
                elif a * b == res:
                    print(f"{edge._from.a} * {edge._from.b} = {edge._to.res}")


solve()
