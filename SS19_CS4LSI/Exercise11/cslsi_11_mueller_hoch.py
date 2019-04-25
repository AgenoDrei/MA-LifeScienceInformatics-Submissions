import random
import time
from dsf import DSF
from graph import Graph
from PIL import Image

def create_graph(g, verts, edges):
	for v in verts:
		g.add_node(v)
	for edge in edges:
		g.add_edge(edge[0], edge[1], edge[2])
		
def create_dsf(d, verts):
	for v in verts:
		d.make_set(v)

def task01(comp, rank):
    NUM_SETS, NUM_OPR = 1000, 500000
    dsf = DSF(comp=comp, rbu=rank)
    for i in range(NUM_SETS):
        dsf.make_set(random.randint(0, 9999))
    
    start = time.time()
    for i in range(NUM_OPR):
        if i % (NUM_OPR // 10) == 0 and i > 0: print("Progress ", i / NUM_OPR)
        dsf_keys = list(dsf.parent.items())
        if random.randint(0, 1) == 0:
            key1, key2 = dsf_keys[random.randint(0, len(dsf_keys)-1)][0], dsf_keys[random.randint(0, len(dsf_keys)-1)][0]
            dsf.union(key1, key2)
        else:
            key = dsf_keys[random.randint(0, len(dsf_keys)-1)][0]
            dsf.find(key)
    end = time.time()
    print('Time: ', end - start)

def task02():
	d = DSF()
	g = Graph()
	create_graph(g, [1, 2, 3, 4, 5], [(1, 2, 1), (1, 3, 3), (1, 5, 4), (2, 3, 2), (2, 4, 4), (3, 4, 4), (3, 5, 5), (4, 5, 2)])
	create_dsf(d, [1, 2, 3, 4, 5])
	
	# Create edge list and sort it
	sorted_edges = []
	for i in g.edges:
		from_node = g.edges[i]
		for conc in from_node:
			sorted_edges.append((i, conc[0], conc[1]))
	sorted_edges.sort(key=lambda x: x[2])
	print("Sorted edges: ", sorted_edges)
	
	#Create minimum spanning tree
	tree_edges = []
	for edge in sorted_edges:
		if d.find(edge[0]) != d.find(edge[1]):
			tree_edges.append(edge)
			d.union(edge[0], edge[1])
	print("Minimum spanning tree: ", tree_edges)


if __name__ == '__main__':
    print("Task 01, Path Compression ON, Union-by-rank ON")
    task01(True, True)
    print()
    print("Task 01, Path Compression OFF, Union-by-rank ON")
    task01(False, True)
    print()
    print("Task 01, Path Compression OFF, Union-by-rank OFF")
    task01(False, False)
    
    print()
    print("Task 02, Create MST according to lecture data")
    print("INFO Edge output format is: (<from_node>, <to_node>, <weight>)")
    task02()
    print("INFO Output is the same as in the slides. It could be slighlty different because there is no fixed procedure if two edges have the same weight. There could be multiple optimal spanning trees. Luckily it does not matter in this case.")
    
    print()
    print("Task 03, general assumption that any edge cannot make the path shorter does not hold anymore. Therefore the greedy approach does not work anymore. counterexample with negative edges: ")
    image = Image.open('task03_a_before.png')
    image.show()
    image2 = Image.open('task03_a_after.png')
    image2.show()
    
    
