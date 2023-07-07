from time import time
from typing import Union
from .tsConstants import TSConstants


class TSBinaryNode:

    def __init__(self, order: Union[float, int] = time(), value=None):
        self.order: Union[float, int] = order
        self.value = value
        self.leftChildNode: Union[TSBinaryNode, None] = None
        self.rightChildNode: Union[TSBinaryNode, None] = None
        self.parentNode: Union[TSBinaryNode, None] = None

    def beautifulPrint(self) -> dict:
        res = {TSConstants.BinaryNode.order: self.order, TSConstants.BinaryNode.value: self.value}
        if self.leftChildNode:
            res[TSConstants.BinaryNode.leftChildNode] = {
                TSConstants.BinaryNode.order: self.leftChildNode.order,
                TSConstants.BinaryNode.value: self.leftChildNode.value
            }
        else:
            res[TSConstants.BinaryNode.leftChildNode] = dict()
        if self.rightChildNode:
            res[TSConstants.BinaryNode.rightChildNode] = {
                TSConstants.BinaryNode.order: self.rightChildNode.order,
                TSConstants.BinaryNode.value: self.rightChildNode.value
            }
        else:
            res[TSConstants.BinaryNode.rightChildNode] = dict()
        if self.parentNode:
            res[TSConstants.BinaryNode.parentNode] = {
                TSConstants.BinaryNode.order: self.parentNode.order,
                TSConstants.BinaryNode.value: self.parentNode.value
            }
        else:
            res[TSConstants.BinaryNode.parentNode] = dict()
        return res
