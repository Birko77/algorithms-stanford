
from collections import defaultdict
import sys
import threading



class DirectedGraph(object):

    def __init__(self, connections):
        self._connections = connections
        # self._graph = defaultdict(set)
        self.add_connections()

        self._search_order = range(len(self._graph), 0, -1)

    def add_connections(self):
        """ Add connections (list of tuple pairs) to graph """

        self._graph = defaultdict(set)

        for node1, node2 in self._connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        self._graph[node2] # need this for nodes that have only incoming arcs


    def add_connections_reverse(self):
        """ Add connections (list of tuple pairs) to graph in reverse """
        """ That means head is tail and  vice versa """

        self._graph = defaultdict(set)

        for node1, node2 in self._connections:
            self.add(node2, node1)



    def DFS_loop(self):

        def DFS(node):
            explored[node] = True
            leaders_and_corresponding_nodes[leader].add(node)
            if len(self._graph[node])>0:
                for child_node in self._graph[node]:
                    if explored[child_node] == False:
                        DFS(child_node)
            nonlocal t
            t += 1
            nodes_processed_in_order.append(node)
            # nodes_processed_in_order.insert(0, node) # add to beginnign of list to get reversed order

        explored = [False] * (len(self._graph)+1)
        nodes_processed_in_order = []
        leaders_and_corresponding_nodes = defaultdict(set)

        t = 1 # number of nodes processed so far: finishing time
        leader = None # current source vertex: leader

        for i in self._search_order:
            if explored[i] == False:
                leader = i
                DFS(i)

        return nodes_processed_in_order, leaders_and_corresponding_nodes

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def get_findable_nodes_DFS(self, start_node):
        found_nodes = []
        return found_nodes

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def get_connections(file_name):

    file = open(file_name, 'r') 

    connections = [[int(num) for num in line.split() if num != '\n'] for line in file ]

    return connections

def get_size_of_five_biggest_components(leaders_and_corresponding_nodes):
    comp_sizes = []
    for key, value in leaders_and_corresponding_nodes.items():
        comp_sizes.append(len(value))
    comp_sizes.sort(reverse=True)
    return comp_sizes[:5]

def main():
    sys.setrecursionlimit(800000)


    connections = get_connections('SCC.txt')

    graph = DirectedGraph(connections)

    graph.add_connections_reverse()

    print('BEFORE FIRST run!')
    # print('Reversed graph:')
    # print(graph)
    # print('search order:')
    # print(graph._search_order)

    nodes_processed_in_order, leaders_and_corresponding_nodes = graph.DFS_loop()

    print('AFTER FIRST run!')
    # print('Nodes prozessed in order:')
    # print(nodes_processed_in_order)

    graph._search_order = reversed(nodes_processed_in_order)

    graph.add_connections()

    print('BEFORE SECOND run!')
    # print('Graph:')
    # print(graph)
    # print('search order:')
    # print(graph._search_order)

    nodes_processed_in_order, leaders_and_corresponding_nodes = graph.DFS_loop()

    print('AFTER SECOND run!')
    print('Leaders and corresponding nodes:')
    print(get_size_of_five_biggest_components(leaders_and_corresponding_nodes))


if __name__ == '__main__':        
    threading.stack_size(67108864)        
    sys.setrecursionlimit(2 ** 20)        
    thread = threading.Thread(target=main)        
    thread.start()
