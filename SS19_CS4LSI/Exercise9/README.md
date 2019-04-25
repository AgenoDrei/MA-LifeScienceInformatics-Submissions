# Assignment 09
- Name: Simon Mueller
- Email: s6simue2@uni-bonn.de

## Exercise 1
#### Subtask d)
Deletion order is not important because it does not change the relationships (greater or smaller) between the nodes. 
- In Case of leaf node deletion you do not change the rest of the tree so the order is unimportant.
- In case of a node with only one child you just replace the node by its child which also leads to the same tree if you switch the order (case 1)
- In case of a node with two childs the firstorder successor does have all the same size relations as the original node so the second delete will affect the same node as if you did it the other way around

#### Subtask e)
inorder for BST

## Exercise 2
#### Subtask a)
This algorithms achieves O(n) running time complexity if i << n: 
```
def simonSelect(list, lo, hi, idx):
    if idx == 1:
        return findMinElm(list)
    ll = hi - lo                #listlength
    resLeft = simonSelect(list, lo, hi - ll, idx/2)
    resRight = simonSelect(list, lo + ll, hi, idx/2)
    return resRight if resRight > resLeft else resLeft 
```
Line 2 has a running time of n / idx and is executed idx times.
The recursion in Line 4 & 5 will be executed log(idx) times.

All in all this results in a running time complexity of O(log(idx) * n)

*Remark* Above implementation only supports idx values of 2^n, could be changed but makes the code more complicated.
 
#### Subtask b)
