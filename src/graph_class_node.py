"""
GRAPH CLASS REALIZATION

matrix presentation + adjacency list presentation
*initially adjacency list presentation is used, but
there is a toMatrix() method to transform it to the
matrix form

* If adjacency list is a dicitonary (not list) then
Node class is not needed

example (not orientated):
vertex:
0: 1 -> 2
1: 0 -> 2
2: 0 -> 1
"""

from stack_class import Stack

class Node:
    def __init__(self, value):
        self._index : int
        self.value = value
        self._in_graph : bool # есть ли вершина уже в графе

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index : int):
        if index >= 0 and isinstance(index, int):
            self._index = index

    @property
    def in_graph(self):
        return self._in_graph

    @in_graph.setter
    def in_graph(self, flag : bool):
        if flag == False or flag == True:
            self._in_graph = flag

class Edge:
    def __init__(self, vertex_start : Node, vertex_end : Node, weight):
        self.start = vertex_start
        self.destination = vertex_end
        self.weight = weight


class Graph:
    def __init__(self, weighted:bool, directed:bool):
        self.numV = -1
        self.adjList = list()
        self.adjMatrix = list()
        self.weighted = weighted
        self.directed = directed


    def addEdge(self, start : Node, finish : Node, w=None):
        # проверям есть ли у вершины индекс, т.е вписана ли она уже в граф
        try:
            self.adjList[start.index].append(Edge(start, finish, w))
        except (KeyError, AttributeError):
            # присвоить вершине новый индекс
            self.numV += 1
            start.index = self.numV
            self.adjList[start.index] = []
            self.adjList[start.index].append(Edge(start, finish, w))

        if not self.directed:
            try:
                self.adjList[finish.index].append(Edge(finish, start, w))
            except (KeyError, AttributeError):
                self.numV += 1
                finish.index = self.numV
                self.adjList[finish.index] = []
                self.adjList[finish.index].append(Edge(finish, start, w))


    def removeVertex(self, vertex : Node):
        # KeyError exception
        try:
            del self.adjList[vertex.index]
            if not self.directed: # для не ориентированного(поэтому симметричного) гарфа
                for v_index in range(len(self.adjList)):
                    for edge in self.adjList[v_index]:
                        if edge.destination == vertex:
                            self.adjList[v_index].remove(edge)
        except KeyError:
            print("No such vertex")
        except AttributeError:
            print("The vertex is not in the graph")


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

    def dfs(self, start_node: int, goal: int):
        """
        поиск в глубину
        * если вершины имеют не только целочисленную характеристику, а более сложную,
        тогда заменить start_node и end_node на класс Node, в котором будут
        храниться все остальные характеристики
        также стоит обратить внимание на строчку 93
        :return:
        """
        next_nodes = Stack()  # узлы, которые нужно посетить
        explored_nodes = set()  # посещенные узлы

        next_nodes.push(start_node)
        explored_nodes.add(start_node)

        while not next_nodes.is_empty():
            node = next_nodes.pop()  # вытаскиваем из стека вершину
            if node == goal:  # заменить в случае *
                print("we have find the vertex: ", end=" ")
                return node
            for n in self.adjList[node]:
                if not n in explored_nodes:
                    next_nodes.push(n)
                    explored_nodes.add(n)
        return None

    def __str__(self):
        """
        prints the graph as adjacency list
        example:
        A: [B, 4] -> [C, 2]
        B: [A, 4]
        C: [A, 2]
        :return: string graph
        """
        answer = ""
        for v_index in range(len(self.adjList)):
            VERTEX = self.adjList[v_index][0].start.value
            answer += str(VERTEX) + ": "
            for edge in self.adjList[v_index]:
                if not self.weighted: # without weights
                    if self.adjList[v_index].index(edge) != (len(self.adjList[v_index]) - 1):
                        answer += "{} -> ".format(edge.destination.value)
                    else:
                        answer += "{}".format(edge.destination.value) + "\n"
                else:
                    if self.adjList[v_index].index(edge) != (len(self.adjList[v_index]) - 1):
                        answer += "{} -> ".format(edge.destination.value)
                    else:
                        answer += "{}".format(edge.destination.value) + "\n"
        return answer

    def printM(self):
        print("Matrix:")
        for i in range(len(self.adjMatrix)):
                print(self.adjMatrix[i])

if __name__ == "__main__":
    my_graph = Graph(weighted=False, directed=False)
    my_graph.addEdge(Node("Anya"), Node("Lera"))
    my_graph.addEdge(Node("Anya"), Node("Masha"))
    my_graph.addEdge(Node("Lera"), Node("Tanya"))


    print(my_graph.adjList)
