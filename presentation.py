import networkx as nx
import matplotlib.pyplot as plt


def show_graph(G):
    G = nx.DiGraph(G)
    pos = nx.random_layout(G)
    nx.draw(G, pos=pos, with_labels=True)
    plt.show()
    return


def print_graph(name, graph: dict):
    print('{}:'.format(name))
    for v1, v2 in graph.items():
        print("{} -> {}".format(v1, v2))
    print()
    return


def print_slides(slides: dict):
    print('slides:')
    for control_leaf, slide in slides.items():
        print('slide({}) = {}'.format(control_leaf, slide))
    print()
    return


def print_buckets(marked, before, after):
    print("""BUCKETS
marked: {}
before: {}
after:  {}
    """.format(marked, before, after))
    return
