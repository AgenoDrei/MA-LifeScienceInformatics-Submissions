from Node import Node
from graphviz import Digraph

class BinaryTree:
    def __init__(self):
        self.root = Node()

    def insert(self, n):
        newNode = Node(n)
        if self.root.value == None:
            self.root = newNode
            return
        self._insert(newNode, self.root)

    def _insert(self, newNode, curNode):
        if newNode <= curNode:
            if curNode.leftChild == None:
                curNode.leftChild = newNode
                newNode.root = curNode
                return
            self._insert(newNode, curNode.leftChild)
        else:
            if curNode.rightChild == None:
                curNode.rightChild = newNode
                newNode.root = curNode
                return
            self._insert(newNode, curNode.rightChild)


    def delete(self, n):
        self._delete(n, self.root)

    def _delete(self, value, curNode):
        delNode = self.search(value)
        if delNode == None:
            return False
        if delNode.leftChild == None and delNode.rightChild == None:                        #Case leaf node
            if value <= delNode.root.value: delNode.root.leftChild = None
            else: delNode.root.rightChild = None
        elif delNode.leftChild == None:                                                     #Case only one child
            if delNode.root.leftChild.value == value: delNode.root.leftChild = delNode.rightChild
            elif delNode.root.rightChild.value == value: delNode.root.rightChild = delNode.rightChild
        elif delNode.rightChild == None:
            if delNode.root.leftChild.value == value: delNode.root.leftChild = delNode.leftChild
            elif delNode.root.rightChild.value == value: delNode.root.rightChild = delNode.leftChild
        elif delNode.leftChild != None and delNode.rightChild != None:                      #Case two childs
            succNode = self._findMin(delNode.rightChild)
            if succNode == None:
                self.root = delNode.leftChild
                return

            if succNode.root.value >= succNode.value: succNode.root.leftChild = None
            else: succNode.root.rightChild = None
            succNode.leftChild = delNode.leftChild
            succNode.rightChild = delNode.rightChild
            succNode.root = delNode.root
            if delNode.root != None:
                if delNode.root.value <= succNode.value: delNode.root.rightChild = succNode
                else: delNode.root.leftChild = succNode
            else:
                self.root = succNode



    def _findMin(self, node):
        if node == None:
            return None
        if node.leftChild == None:
            return node
        return self._findMin(node.leftChild)


    def search(self, n):
        if self.root.value == None:
            return None
        return self._search(Node(n), self.root)

    def _search(self, searchNode, curNode):
        if searchNode.value == curNode.value:
            return curNode

        if searchNode <= curNode:
            if curNode.leftChild == None:
                return None
            return self._search(searchNode, curNode.leftChild)
        else:
            if curNode.rightChild == None:
                return None
            return self._search(searchNode, curNode.rightChild)


    def visualize(self, filename='tree.gv'):
        dot = Digraph(comment='BST', format='png')
        curNode = self.root
        dot.node("{0:.4f}".format(curNode.value))

        self._vis(curNode.leftChild, curNode, dot)
        self._vis(curNode.rightChild, curNode, dot)

        dot.render(filename, view=True)
        return dot

    def _vis(self, node, parent, curGraph):
        if node == None:
            return

        curGraph.node("{0:.4f}".format(node.value))
        curGraph.edge("{0:.4f}".format(parent.value), "{0:.4f}".format(node.value))

        self._vis(node.leftChild, node, curGraph)
        self._vis(node.rightChild, node, curGraph)

    def traverse(self, order='preorder'):
        if order == 'preorder':
            print('Tree traversal preorder: ')
            self._trav_preorder(self.root)
        elif order == 'inorder':
            print('Tree traversal inorder: ')
            self._trav_inorder(self.root)
        elif order == 'postorder':
            print('Tree traversal postorder: ')
            self._trav_postorder(self.root)
        else:
            raise Exception('Invalid traversal order')

    def _trav_preorder(self, node):
        if not node: return
        print(node.value)
        self._trav_preorder(node.leftChild)
        self._trav_preorder(node.rightChild)

    def _trav_inorder(self, node):
        if not node: return
        self._trav_inorder(node.leftChild)
        print(node.value)
        self._trav_inorder(node.rightChild)

    def _trav_postorder(self, node):
        if not node: return
        self._trav_postorder(node.leftChild)
        self._trav_postorder(node.rightChild)
        print(node.value)





