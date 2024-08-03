"""
GRAPH CLASS REALIZATION

matrix presentation + adjacency list presentation
*initially adjacency list presentation is used, but
there is a toMatrix() method to transform it to the
matrix form

example (not orientated):
vertex:
0: 1 -> 2
1: 0 -> 2
2: 0 -> 1
"""

from stack_class import Stack

class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value


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
                print("we have fiund the vertex: ", end=" ")
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
        for key, value in self.adjList.items():
            answer += str(key) + ": "
            if not self.weighted: # without weights
                for edge in value:
                    if value.index(edge) != (len(value) - 1):
                        answer += "{} -> ".format(edge[0])
                    else:
                        answer += "{}".format(edge[0]) + "\n"
            else:
                for edge in value:
                    if value.index(edge) != (len(value) - 1):
                        answer += "{} -> ".format(edge)
                    else:
                        answer += "{}".format(edge) + "\n"
        return answer

    def printM(self):
        print("Matrix:")
        for i in range(len(self.adjMatrix)):
                print(self.adjMatrix[i])

if __name__ == "__main__":
    my_graph = Graph(weighted=False, directed=False)
    my_graph.addEdge(0, 1)
    my_graph.addEdge(0, 2)
    my_graph.addEdge(1, 2)
    print(my_graph)
    print("*removing vertex 2..")
    my_graph.removeVertex(2)
    my_graph.toMatrix()
    my_graph.printM()
    print(my_graph.dfs(0, 2))