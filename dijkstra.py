
from collections import defaultdict
import sys
import threading



class Graph(object):

    def __init__(self, graph):
        self._graph = graph

    



    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def get_graph(file_name):

    file = open(file_name, 'r') 

    graph = defaultdict(set)

    for line in file:
        lst = line.split()
        node = lst[0]
        edges = []
        for i in range(1, len(lst)):
            if lst[i] != '\n':
                edge = [int(string) for string in lst[i].split(',')]
                edges.append(edge)

        graph[node] = edges

    return graph


def main():

    graph = get_graph('dijkstraData.txt')

    print(graph)


if __name__ == '__main__':        
    threading.stack_size(67108864)        
    sys.setrecursionlimit(2 ** 20)        
    thread = threading.Thread(target=main)        
    thread.start()
