from time import time
from typing import Union
from .tsBinaryNode import TSBinaryNode


class TSBinaryHeapNode(TSBinaryNode):

    def __init__(self, order: Union[float, int] = time(), value=None):
        super().__init__(order, value)
        self.index = -1
        self.leftChildNode: Union[TSBinaryHeapNode, None] = None
        self.rightChildNode: Union[TSBinaryHeapNode, None] = None
        self.parentNode: Union[TSBinaryHeapNode, None] = None
