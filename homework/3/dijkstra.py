import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
v1 = 0
v2 = 0
w = 0
labels = {}
V = []
f = open('city.txt', 'r')
for line in f:
    i = list(line.split())
    v1 = i[0]
    v2 = i[1]
    w = i[2]
    G.add_edge(v1, v2, weight = w)
    if v1 not in V:
        V.append(v1)
    if v2 not in V:
        V.append(v2)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=200)
nx.draw_networkx_edges(G, pos, width=3.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8, font_family = 'sans-serif')
v = input()
nx.draw_networkx_nodes(G, pos, nodelist=[v], node_color='r', node_size=200, alpha=0.5)
dij = nx.single_source_dijkstra_path_length(G,v)
nx.draw_networkx_labels(G,pos,dij,font_size=8,font_color='r',font_family = 'sans-serif')
plt.show()