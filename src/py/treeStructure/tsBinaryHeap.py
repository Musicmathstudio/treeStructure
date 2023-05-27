from .tsBinaryHeapNode import TSBinaryHeapNode
from .tsConstants import TSConstants
from typing import Union, Deque
from collections import deque
from math import ceil, floor, log2


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

    def _deleteNodeInDictByOrder(self, order: float):
        if order in self.heapDict:
            self.heapDict[order].popleft()
            if not len(self.heapDict[order]):
                del self.heapDict[order]

    def _compare(self, x, y):
        if self.heapStruct == TSConstants.BinaryHeap.min:
            return x < y
        elif self.heapStruct == TSConstants.BinaryHeap.max:
            return x > y

    def insertNode(self, node: TSBinaryHeapNode):
        self.heapList.append(node)
        self._appendNodeIntoDict(node)
        node.index = len(self.heapList) - 1
        if not node.index:
            node.parentNode = None
        else:
            parentIndex = ceil(node.index / 2) - 1
            parentNode = self.heapList[parentIndex]
            node.parentNode = parentNode
            if node.index % 2:
                parentNode.leftChildNode = node
            else:
                parentNode.rightChildNode = node
            while node.index > 0 and self._compare(node.order, parentNode.order):
                self.heapList[parentIndex], self.heapList[node.index] = \
                    self.heapList[node.index], self.heapList[parentIndex]

                parentNode.index, node.index = node.index, parentNode.index

                if parentNode.leftChildNode == node:
                    node.rightChildNode, parentNode.rightChildNode = parentNode.rightChildNode, node.rightChildNode
                    parentNode.leftChildNode = node.leftChildNode
                    node.leftChildNode = parentNode
                    if node.rightChildNode:
                        node.rightChildNode.parentNode = node
                    if parentNode.rightChildNode:
                        parentNode.rightChildNode.parentNode = parentNode
                    if parentNode.leftChildNode:
                        parentNode.leftChildNode.parentNode = parentNode
                else:
                    node.leftChildNode, parentNode.leftChildNode = parentNode.leftChildNode, node.leftChildNode
                    parentNode.rightChildNode = node.rightChildNode
                    node.rightChildNode = parentNode
                    if node.leftChildNode:
                        node.leftChildNode.parentNode = node
                    if parentNode.leftChildNode:
                        parentNode.leftChildNode.parentNode = parentNode
                    if parentNode.rightChildNode:
                        parentNode.rightChildNode.parentNode = parentNode

                node.parentNode = parentNode.parentNode
                parentNode.parentNode = node

                if node.parentNode.leftChildNode == parentNode:
                    node.parentNode.leftChildNode = node
                else:
                    node.parentNode.rightChildNode = node

                parentIndex = ceil(node.index / 2) - 1
                parentNode = node.parentNode

    def getNodeByOrder(self, order: float) -> Union[TSBinaryHeapNode, None]:
        return self.heapDict.get(order, [None])[0]

    def getTreeHeight(self) -> int:
        nodeCount = len(self.heapList)
        if not nodeCount:
            return -1
        return floor(log2(nodeCount))

    def getTreeNodeCount(self) -> int:
        return len(self.heapList)
