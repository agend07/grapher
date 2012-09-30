# -*- coding: utf-8 -*-

import subprocess
import os
import os.path

import pygraphviz as pgv


directory = '/home/arek/kod/believein/main/templates/'


g = pgv.AGraph()


def first_pass(arg, dirname, names):
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isfile(subname):

            full_name = subname[len(directory):]
            g.add_node(full_name)
            # print 'added node:', full_name


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


# now try to remove nodes which have no neighbours
def remove_lonely_nodes():
    lonely_nodes = []

    for node in g.nodes():
        if not g.neighbors(node):
            lonely_nodes.append(node)

    g.remove_nodes_from(lonely_nodes)


os.path.walk(directory, first_pass, None)
os.path.walk(directory, second_pass, None)
remove_lonely_nodes()

# prog=[‘neato’|’dot’|’twopi’|’circo’|’fdp’|’nop’]
# g.layout()
# g.layout(prog='dot')
g.layout(prog='dot')

g.draw('two.png')
subprocess.call(["eog", "two.png"])
