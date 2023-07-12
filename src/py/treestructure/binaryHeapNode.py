"""
Implementation of binary heap node.
"""

from time import time
from typing import Union
from .binaryNode import BinaryNode


class BinaryHeapNode(BinaryNode):

    def __init__(self, order: Union[float, int] = time(), value=None):
        """
        Binary heap node.

        :param order: It's the priority when constructing the tree structure. Default order is current timestamp.
        :param value: It can be anything you want to store. Default value is None.
        """

        super().__init__(order, value)
        self.index = -1
        self.leftChildNode: Union[BinaryHeapNode, None] = None
        self.rightChildNode: Union[BinaryHeapNode, None] = None
        self.parentNode: Union[BinaryHeapNode, None] = None
