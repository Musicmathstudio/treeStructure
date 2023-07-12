Tree Structure
==============
Tree Structure is a module that implements some common trees in data structure.

# Quick Start
There're two basic component in each type of tree structure: Node and Tree.<br>
Each node has two basic attributes: order and value.<br>
Order is the key to construct the tree structure. Default order is current timestamp.<br>
Value can be anything you want to store. Default value is None.<br>

```
>>> import treestructure
>>> node = treestructure.BinaryNode(35, 'Stevie Wonder') # Create node
>>> node.order
35
>>> node.value
'Stevie Wonder'
```

Insert node into tree to build the tree structure.<br>
Use package() to check the tree structure. It's better using package() with pprint.<br>

```
>>> import pprint
>>> tree = treestructure.BinarySearchTree(node) # Create tree
>>> tree.insertNode(treestructure.BinaryNode(45, 'Ray Charles')) # Insert node
>>> tree.insertNode(treestructure.BinaryNode(25, 'Lionel Richie')) # Insert node
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 35,
 'value': 'Stevie Wonder',
 'leftChildNode': {'order': 25,
                   'value': 'Lionel Richie',
                   'leftChildNode': None,
                   'rightChildNode': None},
 'rightChildNode': {'order': 45,
                    'value': 'Ray Charles',
                    'leftChildNode': None,
                    'rightChildNode': None}}
```

Delete node by specific order.

```
>>> delNode = tree.deleteNode(35) # Delete node
>>> pprint.pprint(delNode.package(), sort_dicts=False) # Display node
{'order': 35,
 'value': 'Stevie Wonder',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {}}
>>> pprint.pprint(tree.package(), sort_dicts=False) # Display tree
{'order': 25,
 'value': 'Lionel Richie',
 'leftChildNode': None,
 'rightChildNode': {'order': 45,
                    'value': 'Ray Charles',
                    'leftChildNode': None,
                    'rightChildNode': None}}
```

# Contents
- Binary Search Tree
- Max/Min Heap
