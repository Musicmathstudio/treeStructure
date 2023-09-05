# Binary Heap

Implementation of binary heap.  
I make some improvement to reduce time complexity of searching node from O(n) to O(1).

## Content

- [Binary Heap](#binary-heap)
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
    - [Transform](#transform)
    - [Merge](#merge)
    - [Clear](#clear)

## Binary Heap

Source code: [binaryHeap.py](https://github.com/Musicmathstudio/treeStructure/blob/main/treestructure/binaryHeap.py)

### Class

---
> treestructure.BinaryHeap(node=None, heapStruct='min')

Module of binary heap.

#### Parameters

- **node**: BinaryNode or None  
  Root node of tree.
- **heapStruct**: str  
  It defines the structure of tree should be min heap or max heap. It can be 'min' or 'max'. Default struct is min heap.

### Insert Node

---
> BinaryHeap.insertNode(node)

Insert node into tree.

#### Parameters

- **node**: BinaryNode  
  node that will be joined.

#### Examples

``` python
>>> node = treestructure.BinaryNode(35, 'John Lee Hooker')
>>> tree = treestructure.BinaryHeap(node) # Create tree
>>> tree.insertNode(treestructure.BinaryNode(25, 'Aretha Franklin')) # Insert node
>>> tree.insertNode(treestructure.BinaryNode(45, 'Bill Withers')) # Insert node
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
```

### Delete Node

---
> BinaryHeap.deleteNode(order)

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
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
 'leftChildNode': {'order': 45,
                   'value': 'Bill Withers',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': None}
```

### Height

---
> BinaryHeap.height()

Tree height.  
If there's no node in tree, height is -1.  
If there's only one node in tree, height is 0.

#### Returns

- **return**: int  
  Tree height.

#### Examples

``` python
>>> tree.package(onlyOrder=True) # Display tree
[25, [35, [None], [None]], [45, [None], [None]]]
>>> tree.height() # Height
1
>>> emptyTree = treestructure.BinaryHeap() # Empty tree
>>> emptyTree.height() # Height
-1
>>> node = treestructure.BinaryNode(10, 'Vanilla Ice')
>>> oneNodeTree = treestructure.BinaryHeap(node) # One node tree
>>> oneNodeTree.height() # Height
0
```

### Node Count

---
> BinaryHeap.nodeCount()

Calculate how many nodes are in tree.

#### Returns

- **return**: int  
  Nodes number in tree.

#### Examples

``` python
>>> tree.package(onlyOrder=True) # Display tree
[25, [35, [None], [None]], [45, [None], [None]]]
>>> tree.nodeCount() # Node count
3
>>> emptyTree = treestructure.BinaryHeap() # Empty tree
>>> emptyTree.nodeCount() # Node count
0
```

### Ordered List

---
> BinaryHeap.orderedList(onlyOrder=False)

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
[25, [35, [None], [None]], [45, [None], [None]]]
>>> orderedList = tree.orderedList() # Ordered list
>>> [node.order for node in orderedList]
[25, 35, 45]
>>> tree.orderedList(onlyOrder=True) # Ordered list only with order
[25, 35, 45]
```

### Get Node By Order

---
> BinaryHeap.getNodeByOrder(order)

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
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
 'leftChildNode': {'order': 35, 'value': 'John Lee Hooker'},
 'rightChildNode': {'order': 45, 'value': 'Bill Withers'},
 'parentNode': {}}
```

### Get Rank By Order

---
> BinaryHeap.getRankByOrder(order)

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
> BinaryHeap.getNodeByRank(rank)

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
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
 'parentNode': {'order': 25, 'value': 'Aretha Franklin'}}
```

### Max Node

---
> BinaryHeap.maxNode()

Get max order node in tree.

#### Returns

- **return**: BinaryNode or None  
  Max order node in tree. Return None if tree is empty.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
 'parentNode': {'order': 25, 'value': 'Aretha Franklin'}}
```

### Min Node

---
> BinaryHeap.minNode()

Get min order node in tree.

#### Returns

- **return**: BinaryNode or None  
  Min order node in tree. Return None if tree is empty.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
 'leftChildNode': {'order': 35, 'value': 'John Lee Hooker'},
 'rightChildNode': {'order': 45, 'value': 'Bill Withers'},
 'parentNode': {}}
```

### Delete Max Node

---
> BinaryHeap.deleteMaxNode()

Delete max order node in tree.

#### Returns

- **return**: BinaryNode or None  
  The node that be removed. Return None if there's no node in tree.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': None}
```

### Delete Min Node

---
> BinaryHeap.deleteMinNode()

Delete min order node in tree.

#### Returns

- **return**: BinaryNode or None  
  The node that be removed. Return None if there's no node in tree.

#### Examples

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
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
 'leftChildNode': {'order': 45,
                   'value': 'Bill Withers',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': None}
```

### Package

---
> BinaryHeap.package(onlyOrder=False)

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
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.package(onlyOrder=True) # Display tree only with order
[25, [35, [None], [None]], [45, [None], [None]]]
>>> emptyTree = treestructure.BinaryHeap() # Empty tree
>>> emptyTree.package() # Display empty tree

>>> emptyTree.package(onlyOrder=True) # Display empty tree only with order
[None]
```

### Transform

---
> BinaryHeap.transform()

Transform heap struct from min heap to max heap/max heap to min heap.

``` python
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Aretha Franklin',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Bill Withers',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.heapStruct # Heap struct
'min'
>>> tree.transform() # Transform
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 45,
 'value': 'Bill Withers',
 'leftChildNode': {'order': 35,
                   'value': 'John Lee Hooker',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 25,
                    'value': 'Aretha Franklin',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree.heapStruct # Heap struct
'max'
```

### Merge

---
> BinaryHeap.merge(tree)

Merge two trees.  
The tree that be merged will be clear.

#### Parameters

- **tree**: BinaryHeap  
  Tree that will be merged.

#### Examples

``` python
>>> pprint.pprint(tree1.package(), sort_dicts=False) # Display tree 1
{'order': 25,
 'value': 'Chic',
 'leftChildNode': {'order': 35,
                   'value': 'The Temptations',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Kool & The Gang',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> pprint.pprint(tree2.package(), sort_dicts=False) # Display tree 2
{'order': 20,
 'value': 'Leann Rimes',
 'leftChildNode': {'order': 30,
                   'value': 'James Brown',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 40,
                    'value': 'Rod Stewart',
                    'leftChildNode': None,
                    'rightChildNode': None}}
>>> tree1.merge(tree2) # Merge two tree
>>> pprint.pprint(tree1.package(), sort_dicts=False) # Desplay tree 1
{'order': 20,
 'value': 'Leann Rimes',
 'leftChildNode': {'order': 25,
                   'value': 'Chic',
                   'leftChildNode': {'order': 35,
                                     'value': 'The Temptations',
                                     'leftChildNode': None,
                                     'rightChildNode': None},
                   'rightChildNode': {'order': 30,
                                      'value': 'James Brown',
                                      'leftChildNode': None,
                                      'rightChildNode': None}},
 'rightChildNode': {'order': 40,
                    'value': 'Rod Stewart',
                    'leftChildNode': {'order': 45,
                                      'value': 'Kool & The Gang',
                                      'leftChildNode': None,
                                      'rightChildNode': None},
                    'rightChildNode': None}}
>>> pprint.pprint(tree2.package(), sort_dicts=False) # Desplay tree 2
None
```

### Clear

---
> BinaryHeap.clear()

Clear tree.

#### Examples

``` python
>>> tree.nodeCount() # Node count
3
>>> tree.clear() # Clear
>>> tree.nodeCount() # Node count
0
```
