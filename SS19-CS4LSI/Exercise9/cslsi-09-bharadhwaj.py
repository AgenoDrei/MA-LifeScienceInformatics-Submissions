from graphviz import Digraph


class BinaryTree():
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insert(self, n):
        if self.root:
            if n < self.root:
                if self.leftChild is None:
                    self.leftChild = BinaryTree(n)
                else:
                    self.leftChild.insert(n)
            elif n > self.root:
                if self.rightChild is None:
                    self.rightChild = BinaryTree(n)
                else:
                    self.rightChild.insert(n)
        else:
            self.root = n

    def delete(self, n):
        if self.root:
            if n == self.root:
                if self.rightChild is None:
                    self.root = self.leftChild.root
                else:
                    self.root = self.rightChild.goLeft(None)
                    self.rightChild.leftChild = None
                    self.leftChild.rightChild = None
            elif n < self.root:
                if self.leftChild is None:
                    print('Value not present')
                else:
                    self.leftChild.delete(n)
            elif n > self.root:
                if self.rightChild is None:
                    print('Value not present')
                else:
                    self.rightChild.delete(n)
        else:
            print('Tree not present')

    def goLeft(self, x):
        self.x = x
        if self.leftChild is None:
            self.x = self.root
            return self.x
        else:
            self.x = self.leftChild.goLeft(self.x)
            return(self.x)

    def search(self, n):
        if self.root:
            if n < self.root:
                if self.leftChild is None:
                    return str(n) + " Not Found"
                return self.leftChild.search(n)
            elif n > self.root:
                if self.rightChild is None:
                    return str(n) + " Not Found"
                return self.rightChild.search(n)
            else:
                return(str(self.root) + ' is found')
        else:
            return str(n) + " Not Found"

    def traverse(self, order, i=0):
        x = None
        if self.root:
            if self.leftChild:
                if self.rightChild:
                    x = [0, self.root, self.leftChild.root, self.rightChild.root]
                else:
                    x = [3, self.root, self.leftChild.root, None]
            else:
                if self.rightChild:
                    x = [2, self.root, None, self.rightChild.root]
                else:
                    x = [23, self.root, None, None]
        if(order == 'pre'):
            print('PreOrder Traversal, Level = {}: {}'.format(i, x[1:]))
            i += 1
            if(x[0] == 0):
                self.leftChild.traverse(order, i)
                self.rightChild.traverse(order, i)
            elif(x[0] == 3):
                self.leftChild.traverse(order, i)
            elif(x[0] == 2):
                self.rightChild.traverse(order, i)
            elif(x[0] == 23):
                print('End of level {}', format(i))
        elif(order == 'in'):
            x[1], x[2] = x[2], x[1]
            print('InOrder Traversal, Level = {}: {}'.format(i, x[1:]))
            i += 1
            if(x[0] == 0):
                self.leftChild.traverse(order, i)
                self.rightChild.traverse(order, i)
            elif(x[0] == 3):
                self.leftChild.traverse(order, i)
            elif(x[0] == 2):
                self.rightChild.traverse(order, i)
            elif(x[0] == 23):
                print('End of level {}', format(i))
        elif(order == 'post'):
            x[1], x[2], x[3] = x[3], x[2], x[1]
            print('PostOrder Traversal, Level = {}: {}'.format(i, x[1:]))
            i += 1
            if(x[0] == 0):
                self.leftChild.traverse(order, i)
                self.rightChild.traverse(order, i)
            elif(x[0] == 3):
                self.leftChild.traverse(order, i)
            elif(x[0] == 2):
                self.rightChild.traverse(order, i)
            elif(x[0] == 23):
                print('End of level {}', format(i))

    def dotgen(self):
        self.dot = Digraph()
        if self.root:
            if self.leftChild:
                if self.rightChild:
                    self.dot.node(str(self.root), str(self.root))
                    self.dot.node(str(self.leftChild.root), str(self.leftChild.root))
                    self.dot.node(str(self.rightChild.root), str(self.rightChild.root))
                    self.dot.edge(str(self.root), str(self.leftChild.root))
                    self.dot.edge(str(self.root), str(self.rightChild.root))
                    temp = self.leftChild.dotgen()
                    for idx, i in enumerate(temp):
                        if(idx == 0 or idx == 1 or i == '}'):
                            continue
                        if('label' in i):
                            self.dot.node(i.split(" [label=", 1)[0][1:], i.split("label=", 1)[1][:-1])
                        elif('->' in i):
                            self.dot.edge(i.split(" ->", 1)[0][1:], i.split(" ->", 1)[1][1:])

                    temp = self.rightChild.dotgen()
                    for idx, i in enumerate(temp):
                        if(idx == 0 or idx == 1 or i == '}'):
                            continue
                        if('label' in i):
                            self.dot.node(i.split(" [label=", 1)[0][1:], i.split("label=", 1)[1][:-1])
                        elif('->' in i):
                            self.dot.edge(i.split(" ->", 1)[0][1:], i.split(" ->", 1)[1][1:])
                    return(self.dot)
                else:
                    self.dot.node(str(self.root), str(self.root))
                    self.dot.node(str(self.leftChild.root), str(self.leftChild.root))
                    self.dot.edge(str(self.root), str(self.leftChild.root))
                    temp = self.leftChild.dotgen()
                    for idx, i in enumerate(temp):
                        if(idx == 0 or idx == 1 or i == '}'):
                            continue
                        if('label' in i):
                            self.dot.node(i.split(" [label=", 1)[0][1:], i.split("label=", 1)[1][:-1])
                        elif('->' in i):
                            self.dot.edge(i.split(" ->", 1)[0][1:], i.split(" ->", 1)[1][1:])
                    return(self.dot)
            else:
                if self.rightChild:
                    self.dot.node(str(self.root), str(self.root))
                    self.dot.node(str(self.rightChild.root), str(self.rightChild.root))
                    self.dot.edge(str(self.root), str(self.rightChild.root))
                    temp = self.rightChild.dotgen()
                    for idx, i in enumerate(temp):
                        if(idx == 0 or idx == 1 or i == '}'):
                            continue
                        if('label' in i):
                            self.dot.node(i.split(" [label=", 1)[0][1:], i.split("label=", 1)[1][:-1])
                        elif('->' in i):
                            self.dot.edge(i.split(" ->", 1)[0][1:], i.split(" ->", 1)[1][1:])
                    return(self.dot)
                else:
                    self.dot.node(str(self.root), str(self.root))
                    return(self.dot)

    def visualize(self, name):
        self.x = self.dotgen()
        self.x.render(name, format='pdf', cleanup=True)


X = BinaryTree(10)
for i in [5, 7, 1, 15, 3, 6, 9, 8, 11]:
    X.insert(i)
print(X.search(14))
print(X.search(7))
X.vizualize('Before_Delete_vis')
X.delete(7)
print(X.search(7))
X.vizualize('After_Delete_vis')
X.traverse('pre')
X.traverse('in')
X.traverse('post')
