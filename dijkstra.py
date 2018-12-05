
from collections import defaultdict
import sys
import threading
import math


class Graph(object):

    def __init__(self, graph):
        self._graph = graph

    def find_shortest_paths(self, source_vertex):
        # initialize BFS
        X = [source_vertex]
        A = {source_vertex : 0}
        queue = [edge[0] for edge in self._graph[source_vertex] if edge not in X]
        print(queue)

        while len(queue) > 0:
            min_score = math.inf
            min_node = None
            for vertex in queue:
                score = self._find_dijkstra_score(vertex, A)
                print('Score of node ' + str(vertex) + ' is ' + str(score))
                if score < min_score:
                    min_score = score
                    min_node = vertex

            A[min_node] = min_score
            X.append(min_node)
            print('Node to remove from queue: ' + str(min_node))
            queue.remove(min_node)

            for node in self._graph[min_node]:
                if node[0] not in X and node[0] not in queue:
                    queue.append(node[0])

            print(queue)

        return A

    def _find_dijkstra_score(self, vertex, A):
        min_score = math.inf
        for node in self._graph[vertex]:
            if node[0] in A:
                current_score = A[node[0]] + node[1]
                if current_score < min_score:
                    min_score = current_score

        return min_score


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def get_graph(file_name):

    file = open(file_name, 'r') 

    graph = defaultdict(set)

    for line in file:
        lst = line.split()
        node = int(lst[0])
        edges = []
        for i in range(1, len(lst)):
            if lst[i] != '\n':
                edge = [int(string) for string in lst[i].split(',')]
                edges.append(edge)

        graph[node] = edges

    return graph

def get_assignment_answer(shortest_paths):

    nodes = [7,37,59,82,99,115,133,165,188,197]

    answer = []

    for node in nodes:
        answer.append(shortest_paths[node])

    return answer

def main():

    graph = Graph(get_graph('dijkstraData.txt'))

    print(graph)

    shortest_paths = graph.find_shortest_paths(1)

    print(get_assignment_answer(shortest_paths))


if __name__ == '__main__':        
    threading.stack_size(67108864)        
    sys.setrecursionlimit(2 ** 20)        
    thread = threading.Thread(target=main)        
    thread.start()
