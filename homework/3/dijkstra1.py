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
v1, v2 = input().split()
path = nx.dijkstra_path(G, v1, v2)
nx.draw_networkx_nodes(G, pos, nodelist=[path], node_color='b', node_size=200, alpha=0.5)
for i in range(0, len(path)-1):
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], width=3.0, alpha=0.5, edge_color='b')
plt.show()