"""
GRAPH ALGORITHMS REALIZATION

+ DFS
+ BFS
"""
from stack_class import Stack
from graph_class import Graph

def dfs(start_node : int, goal : int):
    """
    поиск в глубину
    * если вершины имеют не только целочисленную характеристику, а более сложную,
    тогда заменить start_node и end_node на класс Node, в котором будут
    храниться все остальные характеристики
    также стоит обратить внимание на строчку 27
    :return:
    """
    next_nodes = Stack() # узлы, которые нужно посетить
    explored_nodes = {}  # посещенные узлы

    next_nodes.push(start_node)
    explored_nodes.add(start_node)

    while not next_nodes.is_empty():
        node = next_nodes.pop() # вытаскиваем из стека вершину
        if node == goal: # заменить в случае *
            return node
        for n in self.ad:
            if not n in explored_nodes:
                next_nodes.push(n)
                explored_nodes.add(n)
    return None

