from BinaryTree import BinaryTree
import random

tree = BinaryTree()

#vals = [-31.0016, -83.6916, 59.1930, 67.9372, 76.6732, 54.3413, 48.1884, 76.4714, 65.8254, 24.6577, 74.7057, -84.0207, 96.4194, 14.4067, -94.8019, 3.8470, 5.8980, -66.1468, -66.8983, -63.6209, 74.9514, 77.8144, 60.5814, -15.9487, 38.0042, 5.4400, 60.5719, 44.9556, 57.9557, 96.0428]
vals = [10, 5, 7, 1, 15, 3, 6, 9, 8, 11]
for val in vals:
    tree.insert(val)

tree.visualize(filename='tree1.gv')

#print(tree.search(100))
#tree.delete(59.1930)
#tree.delete(-31.0016)
#tree.delete(5.440)
#tree.delete(-84.0207)
tree.delete(7)
tree.visualize(filename='tree2.gv')
tree.traverse(order='preorder')
tree.traverse(order='inorder')
tree.traverse(order='postorder')
