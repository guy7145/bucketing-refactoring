from bucketing import calculate_sdg, slide_based_bucketing, calculate_leaves
from presentation import print_buckets, print_slides, show_graph
from presentation import print_graph


# input:
from code3 import V, control_edges, data_edges, M


def run_bucketing():
    for g in [data_edges, control_edges]:
        for v in V:
            g[v] = g.get(v, [])

    leaves = calculate_leaves(V, control_edges)
    slides, sdg = calculate_sdg(V, control_edges, data_edges)
    reaching_m, m_reachable, marked, before, after = slide_based_bucketing(V, control_edges, data_edges, M)

    print('control-leaves: {}\n'.format(leaves))

    print('reaching-m:  {}'.format(reaching_m))
    print('m-reachable: {}'.format(m_reachable))
    print()

    print_slides(slides)
    print_graph('sdg', sdg)
    print_buckets(marked, before, after)
    return


run_bucketing()
