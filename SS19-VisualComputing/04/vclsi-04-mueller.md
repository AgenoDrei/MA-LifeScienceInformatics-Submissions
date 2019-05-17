## Exercise 2

### Subtask a)
- For every vertex you store the first and last edge for two linked lists describing outgoing and incoming edges
- Every edge stores similiar values for the next or previous list. Two additonal values are stored that link to its first and second vertex (sink and source)
- If you do not use doubly linked edge list, two values can be ommited (only for 4 for edges)

### Subtask b)
```
def get_edge_idx(u, v):
	for lvl in edge_table_levels:
		outgoing_edge_id = binary_search(edge_table_levels[lvl]['out'], u, attr='Source Vertex')
		edge_id = binary_search(edge_table_levels[lvl]['in'], v, attr='Sink vertex')
		if edge_id == outgoing_edge_id:
			return edge_id
	return None
		 
```
### Subtask c)
- These modifications punish edges that already participate in connections between piviots. This encourages the algorithm to create new piviots in parts of the graph that have not been used so far 
### Subtask d)
- In traversing the graph you can find local and global clusters that place vertices together that are similiar (according to a distance matrix). If you reorder the table accordingly, its much easier to access surrounding edges and vertices. TSP tries to find the shortest way connectiny all nodes. In the progress of finding these paths you can also extract an ordering of edges that represents the local clusters.
### Subtask e)
- ZAME just selects the first label to aggregate all information.
- This is not a good approach because you lose most of the nominal information and ignore everything outside of the intial label. 
### Subtask f)
- Adjacency matrices can get really huge. Storing the full matrix in memory is problematic.
- You split it into tiles of fixed size and load only the relevant ones. Navigation by the user selects the current tiles
- LRU caching removes the tile from memory that has not been used the longest. Every time a tile that is still in memory is reused it will be put in the front of the memory queue. If a new tile has to be used the rear of our queue will be removed and the new one placed in the front. 
### Subtask g)
- Geometric zoom defines the viewport currently seen by the user (continious value)
- Detail zoom defines how much detail the user is shown in the current window (is a discrete parameter)
