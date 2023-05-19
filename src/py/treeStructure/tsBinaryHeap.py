from .tsBinaryHeapNode import TSBinaryHeapNode
from .tsConstants import TSConstants
from typing import Union, Deque
from collections import deque
from math import ceil


class TSBinaryHeap:
    def __init__(self, node: Union[TSBinaryHeapNode, None] = None, heapStruct=TSConstants.BinaryHeap.min):
        self.heapStruct = heapStruct
        self.heapList: Deque[TSBinaryHeapNode] = deque()
        self.heapDict = {}
        if node:
            self.heapList.append(node)
            self.heapDict[node.order] = deque([node])
            node.parentNode = None
            node.index = 0

    def _appendNodeIntoDict(self, node: TSBinaryHeapNode):
        if node.order in self.heapDict:
            self.heapDict[node.order].append(node)
        else:
            self.heapDict[node.order] = deque([node])

    # def insertNode(self, node: TSBinaryHeapNode):
    #     self.heapList.append(node)
    #     self._appendNodeIntoDict(node)
    #     node.index = len(self.heapList) - 1
    #     if not node.index:
    #         node.parentNode = None
    #     else:
    #         nodeCount = len(self.heapList)
    #         parentIndex = ceil(node.index / 2) - 1
    #         parentNode = self.heapList[parentIndex]
    #         node.parentNode = parentNode
    #         if self.heapStruct == TSConstants.BinaryHeap.min:
    #             while not node.index and parentNode.order > node.order:
    #                 self.heapList[parentIndex], self.heapList[node.index] = self.heapList[node.index], self.heapList[parentIndex]
    #                 parentNode.index, node.index = node.index, parentNode.index
    #                 node.parentNode = parentNode.parentNode
    #                 parentNode.parentNode = node
    #
    #                 parentNode.leftChildNode, node.leftChildNode = node.leftChildNode, parentNode.leftChildNode
    #                 parentNode.rightChildNode, node.rightChildNode = node.rightChildNode, parentNode.rightChildNode
    #                 parentIndex = ceil(node.index / 2) - 1
    #                 parentNode = self.heapList[parentIndex]
