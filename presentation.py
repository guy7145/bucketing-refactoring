import networkx as nx
import matplotlib.pyplot as plt


def show_graph(G):
    G = nx.Graph(G)
    pos = nx.random_layout(G)
    nx.draw(G, pos=pos, with_labels=True)
    plt.show()
    return


def print_graph(name, graph):
    print('{}:'.format(name))
    for v1, v2 in graph.items():
        print("{} -> {}".format(v1, v2))
    print()
    return


def print_buckets(marked, before, after):
    print("""BUCKETS

    marked:
    {}

    before:
    {}

    after:
    {}

    """.format(marked, before, after))
    return
