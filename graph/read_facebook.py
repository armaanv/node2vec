import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)
print(nx.info(g))
sp=nx.spring_layout(g)
ply.axis('off')
