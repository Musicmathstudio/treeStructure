"""
Implementation of basic binary node.
"""

from time import time
from typing import Union
from .constants import Constants


class BinaryNode:

    def __init__(self, order: Union[float, int] = time(), value=None):
        """
        Basic binary node.

        :param order: It's the priority when constructing the tree structure. Default order is current timestamp.
        :param value: It can be anything you want to store. Default value is None.
        """

        self._order: Union[float, int] = order
        self.value = value
        self.leftChildNode: Union[BinaryNode, None] = None
        self.rightChildNode: Union[BinaryNode, None] = None
        self.parentNode: Union[BinaryNode, None] = None

    @property
    def order(self) -> Union[float, int]:
        return self._order

    @order.setter
    def order(self, newOrder: Union[float, int] = time()):
        if self.parentNode or self.leftChildNode or self.rightChildNode:
            raise Exception('You can not modify node order if node is already in other tree')
        self._order = newOrder


    def package(self) -> dict:
        """
        Package node information and return.

        :return: A dictionary contains node's order, value, left child, right child and parent.
        """

        res = {Constants.BinaryNode.order: self.order, Constants.BinaryNode.value: self.value}
        if self.leftChildNode:
            res[Constants.BinaryNode.leftChildNode] = {
                Constants.BinaryNode.order: self.leftChildNode.order,
                Constants.BinaryNode.value: self.leftChildNode.value
            }
        else:
            res[Constants.BinaryNode.leftChildNode] = dict()
        if self.rightChildNode:
            res[Constants.BinaryNode.rightChildNode] = {
                Constants.BinaryNode.order: self.rightChildNode.order,
                Constants.BinaryNode.value: self.rightChildNode.value
            }
        else:
            res[Constants.BinaryNode.rightChildNode] = dict()
        if self.parentNode:
            res[Constants.BinaryNode.parentNode] = {
                Constants.BinaryNode.order: self.parentNode.order,
                Constants.BinaryNode.value: self.parentNode.value
            }
        else:
            res[Constants.BinaryNode.parentNode] = dict()
        return res
