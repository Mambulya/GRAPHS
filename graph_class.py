"""
GRAPH CLASS REALIZATION

matrix presentation + adjacency list presentation
*initially adjacency list presentation is used, but
there is a toMatrix() method to transform it to the
matrix form

example (not orientated):
vertex:
0: [1, 4] -> [2, 2]
1: [0, 4]
2: [0, 2]
"""


class Edge:
    def __init__(self, vertex, weight):
        self.destination = vertex
        self.weight = weight


class Graph:
    def __init__(self, weighted:bool, directed:bool):
        self.numV = 0
        self.adjList = dict()
        self.adjMatrix = list()
        self.weighted = weighted
        self.directed = directed

    def addEdge(self, start, finish, w=None):
        try:
            self.adjList[start].append([finish, w])
        except KeyError:
            self.adjList[start] = []
            self.adjList[start].append([finish, w])

        if not self.directed:
            try:
                self.adjList[finish].append([start, w])
            except KeyError:
                self.adjList[finish] = []
                self.adjList[finish].append([start, w])


    def removeVertex(self, vertex):
        # KeyError exception
        try:
            del self.adjList[vertex]
            for k, v in self.adjList.items():
                for edge in v:
                    if edge[0] == vertex:
                        v.remove(edge)
        except KeyError:
            print("No such vertex")


    def toMatrix(self):
        self.adjMatrix = [0] * len(self.adjList)
        for i in range(len(self.adjList)):
            self.adjMatrix[i] = [0] * len(self.adjList)

        for vertex in self.adjList:
            for edge in self.adjList[vertex]:
                if self.weighted:
                    self.adjMatrix[vertex][edge[0]] = edge[1]
                else:
                    self.adjMatrix[vertex][edge[0]] = 1 # if no weight, then 1


    def printL(self):
        """
        prints the graph as adjacency list
        example:
        A: [B, 4] -> [C, 2]
        B: [A, 4]
        C: [A, 2]
        :return:
        """
        for key, value in self.adjList.items():
            print(str(key) + ": ", end="")
            if not self.weighted: # without weights
                for edge in value:
                    if value.index(edge) != (len(value) - 1):
                        print("{} -> ".format(edge[0]), end="")
                    else:
                        print("{}".format(edge[0]))
            else:
                for edge in value:
                    if value.index(edge) != (len(value) - 1):
                        print("{} -> ".format(edge), end="")
                    else:
                        print("{}".format(edge))

    def printM(self):
        print("Matrix:")
        for i in range(len(self.adjMatrix)):
                print(self.adjMatrix[i])

if __name__ == "__main__":
    my_graph = Graph(weighted=False, directed=False)
    my_graph.addEdge(0, 1)
    my_graph.addEdge(0, 2)
    my_graph.addEdge(1, 2)
    my_graph.printL()
    print("*removing vertex 2..")
    my_graph.removeVertex(2)
    my_graph.toMatrix()
    my_graph.printM()