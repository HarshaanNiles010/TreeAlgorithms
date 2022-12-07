# This is an implementation for Dijkstra's single source shortest path algorithm
from queue import PriorityQueue


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.edges = [[-1 for i in range(n)] for j in range(n)]
        self.visited = []

    def add_edge(self, start, end, weight):
        self.edges[start][end] = weight
        self.edges[end][start] = weight


def DSSP(graph, startVertex):
    D = {i: float('inf') for i in range(graph.vertices)}
    D[startVertex] = 0
    pq = PriorityQueue()
    pq.put((0, startVertex))
    while not pq.empty():
        (dist, current) = pq.get()
        graph.visited.append(current)
        for neighbour in range(graph.vertices):
            if graph.edges[current][neighbour] != -1:
                distance = graph.edges[current][neighbour]
                if neighbour not in graph.visited:
                    oldCost = D[neighbour]
                    newCost = D[current] + distance
                    if newCost < oldCost:
                        pq.put((newCost, neighbour))
                        D[neighbour] = newCost
    return D

if __name__ == '__main__':
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)
    D = DSSP(g,8)
    print(D)