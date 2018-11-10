from random import randint
import copy

def get_edges(adj_list):
	edges = []
	for line in adj_list:
		vertex_a = line[0]
		for index, item in enumerate(line):
			if index<1:
				continue
			# remove 'circular edges', this should not be necessary
			if item == vertex_a:
				line.remove(index)

			if item > vertex_a:
				edge = [vertex_a, item]
				edges.append(edge)
	return edges

def get_random_edge(edges):
	num_edges = len(edges)
	return edges[randint(0, num_edges-1)]

def contract(adj_list, edge):
	vertex_a = edge[0]
	vertex_b = edge[1]
	line_a = None
	line_b = None
	for line in adj_list:
		if line[0] == vertex_a:
			line_a = line
		elif line[0] == vertex_b:
			line_b = line

	# delete all references between vertex_a and vertex_b
	# this is the edge that gets contracted and all parallel edges that would become circular edges
	while vertex_b in line_a : line_a.remove(vertex_b)
	while vertex_a in line_b : line_b.remove(vertex_a)

	# add all remaining references from vertex_b to vertex_a
	line_a.extend(line_b[1:])

	# point all references from other vertices to vertex_b to vertex_a
	for line in adj_list:
		for index, item in enumerate(line):
			if item == vertex_b:
				line[index] = vertex_a

	adj_list.remove(line_b)

def get_cut(adj_list):
	while len(adj_list) > 2:
		edges = get_edges(adj_list)
		edge = get_random_edge(edges)
		contract(adj_list, edge)
	return len(adj_list[0])-1

def get_adj_list(file_name):

	file = open(file_name, 'r') 

	adj_list = [[int(num) for num in line.split('\t') if num != '\n'] for line in file ]

	return adj_list

def get_min_cut(adj_list):
	min_cut = 99
	for i in range(400):
		cut = get_cut(copy.deepcopy(adj_list))
		if cut<min_cut:
			min_cut = cut
	return min_cut


adj_list = get_adj_list('kargerMinCut.txt')
# print(adj_list[1:3])
# print(adj_list[15:17])
# edges = get_edges(adj_list)
# random_edge = get_random_edge(edges)
# contract(adj_list, [2,3])
# print(adj_list[1:3])
# print(adj_list[14:16])
# print(edges)
# print(random_edge)
print(get_min_cut(adj_list))
# print(adj_list)