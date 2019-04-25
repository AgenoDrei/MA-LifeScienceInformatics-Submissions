# -*- coding: utf-8 -*-

class Graph:
  def __init__(self):
    # Adjacency list representation
    self.nodes = set()
    self.edges = dict()


  def add_node(self, value):
    self.nodes.add(value)
    self.edges[value]=[]
    
  def add_edge(self, from_node, to_node, weight):
    # Adds an undirected edge (to adjacency lists of from_node and to_node)
    if(not from_node in self.edges.keys()):
        self.edges[from_node]=[]
    
    if(not to_node in self.edges.keys()):
        self.edges[to_node]=[]
        
    self.edges[from_node].append((to_node, weight))
    self.edges[to_node].append((from_node, weight))



  
def bfs(graph, start):
    # Simple example implementation of BFS
    # returns a list of all nodes reachable from start, in breadth-first order
    visited, queue = set(), [start]
    vl=[]
    while queue:
        vertex = queue.pop(0) # Pick nodes from the top
        if vertex not in visited:
            visited.add(vertex)
            vl.append(vertex)
            queue.extend(set(graph.edges[vertex]) - visited) # Add nodes to the end
    return vl


def dfs(graph, start):
    # Simple example implementation of DFS
    # returns a list of all nodes reachable from start, in depth-first order
    visited, stack = set(), [start]
    vl=[]
    while stack:
        vertex = stack.pop() # Get element from the end
        if vertex not in visited:
            visited.add(vertex)
            vl.append(vertex)
            stack.extend(set(graph.edges[vertex]) - visited)# Add elements to the end
        
    return vl
  
'''g=Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_node(7)

g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(2,5)
g.add_edge(6,7)
g.add_edge(6,2)
g.add_edge(6,5)

print ('DFS from node 7:', dfs(g,7))
print ('BFS from node 7:', bfs(g,7))'''

