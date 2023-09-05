"""
Tree Structure is a module that implements some common trees in data structure.

Author: Tony Chiu, Musicmath studio

Email: pi3141592676@yahoo.com.tw

Website: https://github.com/Musicmathstudio/treeStructure

Usage example:

>>> import treestructure
>>> node = treestructure.BinaryNode(35, 'Stevie Wonder') # Create node
>>> node.order
35
>>> node.value
'Stevie Wonder'
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
"""

from .binaryNode import BinaryNode
from .binarySearchTree import BinarySearchTree
from .binaryHeap import BinaryHeap
from .constants import Constants
from .version import __version__
