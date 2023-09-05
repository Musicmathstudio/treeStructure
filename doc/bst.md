# Binary Search Tree

Implementation of basic binary search tree.

## Content

- [Binary Search Tree](#binary-search-tree)
    - [Class](#class)
    - [Insert Node](#insert-node)
    - [Delete Node](#delete-node)
    - [Height](#height)
    - [Node Count](#node-count)
    - [Ordered List](#ordered-list)
    - [Get Node By Order](#get-node-by-order)
    - [Get Rank By Order](#get-rank-by-order)
    - [Get Node By Rank](#get-node-by-rank)
    - [Max Node](#max-node)
    - [Min Node](#min-node)
    - [Delete Max Node](#delete-max-node)
    - [Delete Min Node](#delete-min-node)
    - [Package](#package)
    - [Balance](#balance)
    - [Merge](#merge)
    - [Clear](#clear)

## Binary Search Tree

Source
code: [binarySearchTree.py](https://github.com/Musicmathstudio/treeStructure/blob/main/treestructure/binarySearchTree.py)

### Class

---
> treestructure.BinarySearchTree(node=None)

Module of binary search tree.

#### Parameters

- **node**: BinaryNode or None  
  Root node of tree.

### Insert Node

---
> BinarySearchTree.insertNode(node)

Insert node into tree.

#### Parameters

- **node**: BinaryNode  
  node that will be joined.

#### Examples

``` python
>>> node = treestructure.BinaryNode(35, 'John Lee Hooker')
>>> tree = treestructure.BinarySearchTree(node) # Create tree
>>> tree.insertNode(treestructure.BinaryNode(25, 'Aretha Franklin')) # Insert node
>>> tree.insertNode(treestructure.BinaryNode(45, 'Bill Withers')) # Insert node
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
```

### Delete Node

---
> BinarySearchTree.deleteNode(order)

Delete node by order.

#### Parameters

- **order**: float or int  
  Delete a node with giving order.

#### Returns

- **return**: BinaryNode or None  
  The node that be removed. Return None if there's no node with giving order.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> delNode = tree.deleteNode(35) # Delete node
>>> pprint.pprint(delNode.package(), sort_dicts=False) # Display node
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {}}
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': None,
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
```

### Height

---
> BinarySearchTree.height()

Tree height.  
If there's no node in tree, height is -1.  
If there's only one node in tree, height is 0.

#### Returns

- **return**: int  
  Tree height.

#### Examples

``` python
>>> tree.package(onlyOrder=True) # Display tree
[35, [25, [None], [None]], [45, [None], [None]]]
>>> tree.height() # Height
1
>>> emptyTree = treestructure.BinarySearchTree() # Empty tree
>>> emptyTree.height() # Height
-1
>>> node = treestructure.BinaryNode(10, 'Vanilla Ice')
>>> oneNodeTree = treestructure.BinarySearchTree(node) # One node tree
>>> oneNodeTree.height() # Height
0
```

### Node Count

---
> BinarySearchTree.nodeCount()

Calculate how many nodes are in tree.

#### Returns

- **return**: int  
  Nodes number in tree.

#### Examples

``` python
>>> tree.package(onlyOrder=True) # Display tree
[35, [25, [None], [None]], [45, [None], [None]]]
>>> tree.nodeCount() # Node count
3
>>> emptyTree = treestructure.BinarySearchTree() # Empty tree
>>> emptyTree.nodeCount() # Node count
0
```

### Ordered List

---
> BinarySearchTree.orderedList(onlyOrder=False)

Sort node by order.

#### Parameters

- **onlyOrder**: bool  
  Return array only contains order if onlyOrder is True. Default is False.

#### Returns

- **return**: List of BinaryNode, float or int  
  Sorted list.

#### Examples

``` python
>>> tree.package(onlyOrder=True) # Display tree
[35, [25, [None], [None]], [45, [None], [None]]]
>>> orderedList = tree.orderedList() # Ordered list
>>> [node.order for node in orderedList]
[25, 35, 45]
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
```

### Get Node By Order

---
> BinarySearchTree.getNodeByOrder(order)

Search a node with giving order.

#### Parameters

- **order**: float or int  
  Node order.

#### Returns

- **return**: BinaryNode or None  
  Node with giving order. Return None if there's no node with giving order.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> node = tree.getNodeByOrder(25) # Get node by order
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {'order': 35, 'value': 'John Lee Hooker'}}
```

### Get Rank By Order

---
> BinarySearchTree.getRankByOrder(order)

Check the rank of node in sorted list with specific order. Rank start with 0.  
If there's no node with giving order. Rank is -1.

#### Parameters

- **order**: float or int  
  Node order.

#### Returns

- **return**: BinaryNode or None  
  Rank of node in sorted list. Return -1 if there's no node with giving order.

#### Examples

``` python
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
>>> tree.getRankByOrder(35) # Get rank by order
1
>>> tree.getRankByOrder(85) # Get rank by order
-1
```

### Get Node By Rank

---
> BinarySearchTree.getNodeByRank(rank)

Get node by giving rank in sorted list.

#### Parameters

- **rank**: int  
  Rank in sorted list.

#### Returns

- **return**: BinaryNode or None  
  Node in tree. Return None if rank < 0 or rank >= node count.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
>>> node = tree.getNodeByRank(2) # Get node by rank
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 45,
 'value': 'Bill Withers',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {'order': 35, 'value': 'John Lee Hooker'}}
```

### Max Node

---
> BinarySearchTree.maxNode()

Get max order node in tree.

#### Returns

- **return**: BinaryNode or None  
  Max order node in tree. Return None if tree is empty.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
>>> node = tree.maxNode() # Max node
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 45,
 'value': 'Bill Withers',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {'order': 35, 'value': 'John Lee Hooker'}}
```

### Min Node

---
> BinarySearchTree.minNode()

Get min order node in tree.

#### Returns

- **return**: BinaryNode or None  
  Min order node in tree. Return None if tree is empty.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
>>> node = tree.minNode() # Min node
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {'order': 35, 'value': 'John Lee Hooker'}}
```

### Delete Max Node

---
> BinarySearchTree.deleteMaxNode()

Delete max order node in tree.

#### Returns

- **return**: BinaryNode or None  
  The node that be removed. Return None if there's no node in tree.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
>>> node = tree.deleteMaxNode() # Delete max node
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 45,
 'value': 'Bill Withers',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {}}
>>> pprint.pprint(tree.package(), sort_dicts=False)  # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': None}
```

### Delete Min Node

---
> BinarySearchTree.deleteMinNode()

Delete min order node in tree.

#### Returns

- **return**: BinaryNode or None  
  The node that be removed. Return None if there's no node in tree.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
>>> node = tree.deleteMinNode() # Delete min node
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {}}
>>> pprint.pprint(tree.package(), sort_dicts=False)  # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': None,
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
```

### Package

---
> BinarySearchTree.package(onlyOrder=False)

Package tree structure and return.

#### Parameters

- **onlyOrder**: bool  
  Return tree only contains order in each node if onlyOrder is True. Default is False.

#### Returns

- **return**: dict, list or None  
  Tree structure as dictionary.  
  Return type is list if onlyOrder is True.  
  Return None if tree is empty.  
  Return [None] if tree is empty and onlyOrder is True.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'John Lee Hooker',
 'leftChildNode': {'order': 25,
                   'value': 'Aretha Franklin',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.package(onlyOrder=True) # Display tree only with order
[35, [25, [None], [None]], [45, [None], [None]]]
>>> emptyTree = treestructure.BinarySearchTree() # Empty tree
>>> emptyTree.package() # Display empty tree

>>> emptyTree.package(onlyOrder=True) # Display empty tree only with order
[None]
```

### Balance

---
> BinarySearchTree.balance()

Make tree balance.

#### Examples

``` python
>>> tree.package(onlyOrder=True) # Display tree
[25, [None], [35, [None], [45, [None], [None]]]]
>>> tree.height() # Height
2
>>> tree.balance() # Balance
>>> tree.package(onlyOrder=True)
[35, [25, [None], [None]], [45, [None], [None]]]
>>> tree.height()  # Height
1
```

### Merge

---
> BinarySearchTree.merge(tree)

Merge two trees.  
The tree that be merged will be clear.

#### Parameters

- **tree**: BinarySearchTree  
  Tree that will be merged.

#### Examples

``` python
>>> pprint.pprint(tree1.package(), sort_dicts=False) # Display tree 1
{'order': 35,
 'value': 'The Temptations',
 'leftChildNode': {'order': 25,
                   'value': 'Chic',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Kool & The Gang',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> pprint.pprint(tree2.package(), sort_dicts=False) # Display tree 2
{'order': 30,
 'value': 'James Brown',
 'leftChildNode': {'order': 20,
                   'value': 'Leann Rimes',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 40,
                    'value': 'Rod Stewart',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree1.merge(tree2) # Merge two tree
>>> pprint.pprint(tree1.package(), sort_dicts=False) # Desplay tree 1
{'order': 35,
 'value': 'The Temptations',
 'leftChildNode': {'order': 25,
                   'value': 'Chic',
                   'leftChildNode': {'order': 20,
                                     'value': 'Leann Rimes',
                                     'leftChildNode': None,
                                     'rightChildNode': None},
                   'rightChildNode': {'order': 30,
                                      'value': 'James Brown',
                                      'leftChildNode': None,
                                      'rightChildNode': None}},
 'rightChildNode': {'order': 45,
                    'value': 'Kool & The Gang',
                    'leftChildNode': {'order': 40,
                                      'value': 'Rod Stewart',
                                      'leftChildNode': None,
                                      'rightChildNode': None},
                    'rightChildNode': None}}
>>> pprint.pprint(tree2.package(), sort_dicts=False) # Desplay tree 2
None
```

### Clear

---
> BinarySearchTree.clear()

Clear tree.

#### Examples

``` python
>>> tree.nodeCount() # Node count
3
>>> tree.clear() # Clear
>>> tree.nodeCount() # Node count
0
```
