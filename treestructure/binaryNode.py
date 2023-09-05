"""
Module of basic binary node.
"""

from time import time
from typing import Union, Any
from .constants import Constants


class BinaryNode:

    def __init__(self, order: Union[float, int] = time(), value=None):
        """
        Module of basic binary node.

        :param order: It's the priority when constructing the tree structure. Default order is current timestamp.
        :param value: It can be anything you want to store. Default value is None.
        """

        self._typeCheck(order)
        self._order: Union[float, int] = order
        self._value: Any = value
        self._leftChildNode: Union[BinaryNode, None] = None
        self._rightChildNode: Union[BinaryNode, None] = None
        self._parentNode: Union[BinaryNode, None] = None
        self._index = -1
        self._inTree = False

    @property
    def order(self) -> Union[float, int]:
        return self._order

    @order.setter
    def order(self, newOrder: Union[float, int]):
        if self._inTree:
            raise Exception('You can not modify node order if node is already in other tree')
        self._typeCheck(newOrder)
        self._order = newOrder

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, newValue: Any):
        self._value = newValue

    @property
    def leftChildNode(self) -> Union['BinaryNode', None]:
        return self._leftChildNode

    @property
    def rightChildNode(self) -> Union['BinaryNode', None]:
        return self._rightChildNode

    @property
    def parentNode(self) -> Union['BinaryNode', None]:
        return self._parentNode

    def _typeCheck(self, order: Union[float, int]):
        if type(order) not in (float, int):
            raise Exception('Type of order should be float or int')

    def package(self) -> dict:
        """
        Package node information and return.

        :return: A dictionary contains node's order, value, left child, right child and parent.
        """

        res = {Constants.BinaryNode.order: self._order, Constants.BinaryNode.value: self._value}
        if self._leftChildNode:
            res[Constants.BinaryNode.leftChildNode] = {
                Constants.BinaryNode.order: self._leftChildNode._order,
                Constants.BinaryNode.value: self._leftChildNode._value
            }
        else:
            res[Constants.BinaryNode.leftChildNode] = dict()
        if self._rightChildNode:
            res[Constants.BinaryNode.rightChildNode] = {
                Constants.BinaryNode.order: self._rightChildNode._order,
                Constants.BinaryNode.value: self._rightChildNode._value
            }
        else:
            res[Constants.BinaryNode.rightChildNode] = dict()
        if self._parentNode:
            res[Constants.BinaryNode.parentNode] = {
                Constants.BinaryNode.order: self._parentNode._order,
                Constants.BinaryNode.value: self._parentNode._value
            }
        else:
            res[Constants.BinaryNode.parentNode] = dict()
        return res
