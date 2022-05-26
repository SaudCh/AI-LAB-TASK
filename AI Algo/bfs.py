from queue import PriorityQueue
import timeit as t
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):

        self.graph = {
            "A": [(130, ("A", "O")), (110, ("A", "S")), (420, ("A", "C"))],
            "O": [(105, ("O", "A")), (108, ("O", "S"))],
            "S": [(101, ("S", "O")), (111, ("S", "A")), (80, ("S", "R")), (99, ("S", "F"))],
            "C": [(494, ("C", "A")), (146, ("C", "R"))],
            "R": [(80, ("R", "S")), (146, ("R", "C")), (97, ("R", "P"))],
            "F": [(99, ("F", "S")), (211, ("F", "B"))],
            "B": [(211, ("B", "F")), (101, ("B", "P"))],
            "P": [(101, ("P", "B")), (97, ("P", "R")), (138, ("P", "C"))]}
        self.heristics = {
            "A": 10,
            "O": 9,
            "S": 7,
            "C": 8,
            "R": 6,
            "F": 5,
            "P": 3,
            "B": 0
        }
        self.edges = {}
        self.weights = {}
        self.fill_edges()
        self.fill_weights()

        print("edges : ", self.edges)
        print("------------------------------------")
        print("weights  : ", self.weights)

    def fill_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
                neighbours.append(each_tuple[1][1])
            self.edges[key] = neighbours

    def fill_weights(self):
        for key in self.graph:
            neighbours = self.graph[key]
            for each_tuple in neighbours:
                self.weights[each_tuple[1]] = each_tuple[0]

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]

    def get_heuristic(self, node):
        return self.heristics[node]
    
def bfs(graph, start, goal):
    explored = []
    queue = PriorityQueue()
    queue.put((0,start))
    while queue:
        cost, node = queue.get()
        print('node being explored: ', node)
        print("explored : ", explored)
        if node not in explored:
            explored.append(node)
            if node == goal:
                break
            neighbours = graph.neighbors(node)
            for neighbour in neighbours:
                total_cost = graph.get_cost(node, neighbour)
                queue.put((total_cost,neighbour))
    return explored

startTime = t.default_timer()
print("BFS Traversal : ", bfs(Graph(), "A", "B"))
endTime = t.default_timer()
totalTime = [endTime-startTime]