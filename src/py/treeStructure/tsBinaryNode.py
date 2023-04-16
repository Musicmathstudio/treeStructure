import time
from typing import Union


class TSBinaryNode:

    def __init__(self, order: float = time.time(), value=None):
        self.order: float = float(order)
        self.value = value
        self.leftChildNode: Union[TSBinaryNode, None] = None
        self.rightChildNode: Union[TSBinaryNode, None] = None
        self.parentNode: Union[TSBinaryNode, None] = None

    def beautifulPrint(self) -> dict:
        res = {'order': self.order, 'value': self.value}
        if self.leftChildNode:
            res['leftChildNode'] = {'order': self.leftChildNode.order, 'value': self.leftChildNode.value}
        else:
            res['leftChildNode'] = dict()
        if self.rightChildNode:
            res['rightChildNode'] = {'order': self.rightChildNode.order, 'value': self.rightChildNode.value}
        else:
            res['rightChildNode'] = dict()
        if self.parentNode:
            res['parentNode'] = {'order': self.parentNode.order, 'value': self.parentNode.value}
        else:
            res['parentNode'] = dict()
        return res
