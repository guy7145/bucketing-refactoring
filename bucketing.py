import itertools


SEARCH_FORWARD = 'FORWARD'
SEARCH_BACKWARD = 'BACKWARD'


def calculate_leaves(V: set, control_edges: dict):
    leaves = list()
    for v in V:
        if len(control_edges[v]) == 0:
            leaves.append(v)
    return sorted(leaves)


def reverse_edge(src, trgt):
    return (trgt, src)


def reverse_graph(E: dict):
    E_reversed = {v: [] for v in E.keys()}
    for src, targets in E.items():
        for trgt in targets:
            E_reversed[trgt].append(src)
    return E_reversed


def record_bfs(graph: dict, src_nodes: set):
    recorded_nodes = set()

    current_sources = src_nodes.copy()
    while len(current_sources) > 0:
        src = current_sources.pop()
        recorded_nodes.add(src)
        current_sources.update(graph[src])
        current_sources.difference_update(recorded_nodes)

    return recorded_nodes


def calculate_slide(control_edges: dict, leaf):
    reverse_edges = reverse_graph(control_edges)
    return sorted(record_bfs(reverse_edges, {leaf}))


def calculate_slides(V: set, control_edges: dict):
    leaves = calculate_leaves(V, control_edges)
    slides = dict()
    for l in leaves:
        slides[l] = calculate_slide(control_edges, l)
    return slides


def calculate_sdg(V: set, control_edges: dict, data_edges: dict):
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
    return slides, sdg


def slides_first_search(sdg: dict, target_nodes, search_direction):
    if search_direction == SEARCH_BACKWARD:
        edges = reverse_graph(sdg)
    else:
        edges = sdg

    return record_bfs(edges, target_nodes)


def union_slides(leaves: set, slides: dict):
    union = set()
    for l in leaves:
        union.update(slides[l])
    return union


def slide_based_bucketing(V: set, control_edges: dict, data_edges: dict, M: set):
    slides, sdg = calculate_sdg(V, control_edges, data_edges)

    m_reachable = slides_first_search(sdg, M, SEARCH_FORWARD)
    reaching_m = slides_first_search(sdg, M, SEARCH_BACKWARD)

    print("reaching_m:")
    print(reaching_m)
    print("m_reachable:")
    print(m_reachable)

    marked = reaching_m.intersection(m_reachable)
    before = reaching_m.difference(m_reachable)
    after = m_reachable.difference(reaching_m)

    return reaching_m, m_reachable,\
           union_slides(marked, slides), \
           union_slides(before, slides), \
           union_slides(after, slides)
