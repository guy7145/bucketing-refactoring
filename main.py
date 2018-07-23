from bucketing import *


V = {465, 466, 467, 469, 470, 473, 474, 475, 476, 480, 481, 483, 484, 485, 487, 488, 490, 491, 495}
control_edges = {
	466: [467, 469],
	469: [470, 473, 474, 475],
	475: [476, 480, 481, 483],
	483: [484, 485, 487],
	487: [488, 490, 491]
}
for v in V:
	control_edges[v] = control_edges.get(v, [])

data_edges = {
	465: [467, 470, 481],
	467: [495],
	470: [495],
	473: [480, 476],
	474: [476],
	475: [475],
	476: [476],
	480: [481, 485, 491],
	481: [483, 485, 487, 491, 495],
	484: [485, 495],
	487: [490],
	490: [491, 495]	
}
for v in V:
	data_edges[v] = data_edges.get(v, [])
	
	
print("leaves:\n{}".format(calculate_leaves(V, control_edges)))
print()
print("slides:")
for v, slide in calculate_slides(V, control_edges).items():
	print("slide({}) = {}".format(v, slide))

print("sdg:")
for s1, s2 in calculate_sdg(V, control_edges, data_edges).items():
	print("{} -> {}".format(s1, s2))

show_graph(data_edges)
