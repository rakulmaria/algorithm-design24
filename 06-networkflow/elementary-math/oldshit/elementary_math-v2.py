
from queue import Queue
from sys import stdin

class Node():
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.adjacentEdges = {}
        self.isSource = source
        self.isSink = sink

    def addEdge(self, edge):
        self.adjacentEdges.update({edge: edge})
        

class Edge():
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to
        self._capacity = 1
        self._flow = 0

    def updateCapacity(self):
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
            
        if self.getNode(node) == None:
            self.mapOfNodes.update({node.id: node})

    def getNode(self, node):
        return self.mapOfNodes.get(node.id)

    def getEdge(self, edge):
        return self.mapOfEdges.get((edge._from.id, edge._to.id))

    def addEdge(self, edge):
        thisEdge = self.getEdge(edge)

        if thisEdge is None:
            self.mapOfEdges.update({(edge._from.id, edge._to.id): edge})
            # update the from and to nodes
            self.getNode(edge._from).addEdge(edge)
            self.getNode(edge._to).addEdge(edge)
        else:
            thisEdge.updateCapacity()
            self.getNode(edge._from).addEdge(self.getEdge(thisEdge))
            self.getNode(edge._to).addEdge(self.getEdge(thisEdge))
        
    def connectNodesToSink(self, nodes):
        for node in nodes:
            if self.mapOfEdges.get((node.id, self.sink.id)) == None:
                e = Edge(node, graph.getNode(self.sink))
                self.addEdge(e)
    
    def printGraph(self):

        print(f"NODES: {len(self.mapOfNodes)}")
        print()
        for node in self.mapOfNodes.values():
            print(f"{node.id}")
            for e in node.adjacentEdges.values():
                print("  ", end="")
                e.printEdge()

        print()
        print(f"EDGES: {len(self.mapOfEdges)}")
        print()
        for edge in self.mapOfEdges.values():
            edge.printEdge()

    def getGraphSize(self):
        return len(self.mapOfNodes)
            

    def findPath(self, _from: Node, _to: Node):
        markedNodes = {}
        queue = Queue(maxsize=graph.getGraphSize())
        print(f"Queue: {queue}")
        
        markedNodes[_from.id] = True 

        queue.put(item=_from)             # and put it on the queue

        while not queue.empty():
            currentNode = queue.get()
            print(f"currentNode: {currentNode}")
            
            for edge in currentNode.adjacentEdges:
                print(f"currentNode's adjacentEdge: {edge}")
                otherNode = edge.getOther(currentNode)
                print(f"currentNode's getOher: {otherNode}")

                if edge.residualCapacityTo(otherNode) > 0 and not markedNodes.get(otherNode.id):
                    print(f"we haven't marked this node yet and there is still capacity on it")
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
    
    def result(self):
        filteredEdges = []
        result = []
        for edge in self.mapOfEdges.values():
            if edge._from.id != "source" and edge._flow > 0 and edge._to.id != "sink":
                filteredEdges.append(edge)

        for edge in filteredEdges:
            res = edge._to.id
            a = edge._from.id[0]
            b = edge._from.id[1]

            if a + b == res:
                res = f"{a} + {b} = {res}"
            elif a - b == res:
                res = f"{a} - {b} = {res}"
            elif a * b == res:
                res = f"{a} * {b} = {res}"
            result.append(res)

        for r in result:
            print(r)


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

    p = Node(a + b)
    m = Node(a - b)
    t = Node(a * b)
    # why does node 1 not have adjacent edges, how do I create them

    graph.addNode(n1)
    graph.addNode(p)
    graph.addNode(m)
    graph.addNode(t)
    e0 = Edge(graph.getNode(sourceNode), graph.getNode(n1))

    e1 = Edge(n1, p)
    e2 = Edge(n1, m)
    e3 = Edge(n1, t)


    graph.addEdge(e0)
    graph.addEdge(e1)
    graph.addEdge(e2)
    graph.addEdge(e3)
    graph.connectNodesToSink([p, m, t])


graph.printGraph()

print(f"maxflow is: {graph.findMaxFlow()}")

graph.printGraph()

#graph.result()