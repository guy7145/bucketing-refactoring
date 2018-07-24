from bucketing import calculate_sdg, slide_based_bucketing, calculate_leaves
from presentation import print_buckets
from presentation import print_graph

# input:
from example2 import V, control_edges, data_edges, M

for g in [data_edges, control_edges]:
        for v in V:
            g[v] = g.get(v, [])

leaves = calculate_leaves(V, control_edges)
slides, sdg = calculate_sdg(V, control_edges, data_edges)
marked, before, after = slide_based_bucketing(V, control_edges, data_edges, M)

print('leaves: {}\n'.format(leaves))

print_graph('slides', slides)
print_graph('sdg', sdg)
print_buckets(marked, before, after)
