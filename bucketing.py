import itertools
import networkx as nx
import matplotlib.pyplot as plt


def show_graph(G):
	G = nx.Graph(G)
	pos = nx.random_layout(G)
	nx.draw(G,pos=pos, with_labels=True)
	plt.show()
	return

def calculate_leaves(V, control_graph):
	leaves = list()
	for v in V:
		if len(control_graph[v]) == 0:
			leaves.append(v)
	return sorted(leaves)

def reverse_edge(src, trgt):
	return (trgt, src)

def reverse_graph(V, E):
	E_reversed = {l: [] for l in V}
	for src, targets in E.items():
		for trgt in targets:
			E_reversed[trgt].append(src)
	return E_reversed

def calculate_slide(src, reverse_edges):
	# input is a tree
	slide = set()
	current_sources = {src}
	while len(current_sources) > 0:
		src = current_sources.pop()
		slide.add(src)
		current_sources.update(reverse_edges[src])
	return sorted(slide)

def calculate_slides(V, control_edges):
	leaves = calculate_leaves(V, control_edges)
	reverse_edges = reverse_graph(V, control_edges)
	slides = dict()
	for l in leaves:
		slides[l] = calculate_slide(l, reverse_edges)
	return slides

def calculate_sdg(V, control_edges, data_edges):
	slides = calculate_slides(V, control_edges)
	leaves = list(slides.keys())
	sdg = {l: [] for l in leaves}
	
	for l1, l2 in itertools.product(leaves, leaves):
		for s1, s2 in itertools.product(slides[l1], slides[l2]):
			if s2 in data_edges[s1]:
				sdg[l1].append(l2)
				break
	
	for l in sdg.keys():
		sdg[l] = sorted(sdg[l])
	return sdg
