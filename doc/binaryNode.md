# Binary Node

Basic unit in each type of binary tree.

## Content

- [Binary Node](#binary-node)
    - [Class](#class)
    - [Package](#package)

## Binary Node

Source code: [binaryNode.py](https://github.com/Musicmathstudio/treeStructure/blob/main/treestructure/binaryNode.py)

### Class

---
> treestructure.BinaryNode(order=time.time(), value=None)

Module of basic binary node.

#### Parameters

- **order**: float or int  
  It's the priority when constructing the tree structure. Default order is current timestamp.
- **value**: Any  
  It can be anything you want to store. Default value is None.
- **leftChildNode**: BinaryNode or None  
  Save the pointer points to left node.
- **rightChildNode**: BinaryNode or None  
  Save the pointer points to right node.
- **parentNode**: BinaryNode or None  
  Save the pointer points to parent node.
  > Note: You can't modify order if node has been added into tree. It'll raise error.  
    leftChildNode, rightChildNode and parentNode are read-only.  
    You can edit value anytime.

### Package

---
> BinaryNode.package()

Package node information and return.

#### Returns

- **return**: dict  
  A dictionary contains node's order, value, left child, right child and parent.

#### Examples

``` python
>>> node = treestructure.BinaryNode(25, 'Michael Jackson') # Create node
>>> node.order
25
>>> node.value
'Michael Jackson'
>>> pprint.pprint(node.package(), sort_dicts=False) # Display node
{'order': 25,
 'value': 'Michael Jackson',
 'leftChildNode': {},
 'rightChildNode': {},
 'parentNode': {}}
>>> node.order = 35 # Modify node
>>> node.value = 'Prince' # Modify node
>>> node.order
35
>>> node.value
'Prince'
```