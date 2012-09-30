import subprocess
import os
import os.path


import networkx as nx
import matplotlib.pyplot as plt
# import pygraphviz

g = nx.Graph()

# nx.draw_graphviz(g)
# nx.write_dot(g, 'graph.dot')

directory = '/home/arek/kod/believein/main/templates/'


def first_pass(arg, dirname, names):
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isfile(subname):

            full_name = subname[len(directory):]
            g.add_node(full_name)
            print 'added node:', full_name


def second_pass(arg, dirname, names):
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isfile(subname):
            with open(subname) as f:
                line = f.readline().strip()

                if line.startswith('{% extends'):

                    full_name = subname[len(directory):]
                    parent = line.split()[2].strip('"\'')

                    g.add_edge(parent, full_name)
                    # print name, '->', parent


os.path.walk(directory, first_pass, None)
os.path.walk(directory, second_pass, None)


# nx.draw(g)
# plt.savefig('normal.png')

nx.spectral_layout(g, scale=.5)
nx.draw(g, scale=.1000)
plt.savefig('cos.png')
subprocess.call(["eog", "cos.png"])


# nx.draw_circular(g)
# plt.savefig('circular.png')
# nx.draw_spectral(g)
# plt.savefig('spectral.png')

# nx.draw_circular(g)
# plt.savefig('templates.png')
# subprocess.call(["eog", "templates.png"])

# draw graph
# nx.draw(g)
# plt.savefig('templates.png')

# nx.draw_graphviz(g)
# nx.write_dot(g, 'templates.dot')
# subprocess.call(["eog", "templates.png"])

# print 'nodes', g.nodes()
# print
# print
# print 'edges', g.edges()
