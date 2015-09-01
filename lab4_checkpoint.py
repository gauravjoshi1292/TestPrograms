# lab4_checkpoint.py
# CS 1 Lab Assignment #4 checkpoint by THC.
# Creates a dictionary of Vertex objects based on reading in a file.
# Writes out a string for each Vertex object to a file.

from load_graph import load_graph
from bfs import breadth_first_search

vertex_dict = load_graph("dartmouth_graph.txt")

out_file = open("vertices.txt", "w")
for vertex in vertex_dict:
    out_file.write(str(vertex_dict[vertex]) + "\n")
out_file.close()

start = vertex_dict["Rocky"]
goal = vertex_dict["AXA"]
print breadth_first_search(start, goal)