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

    def _compare(self, x: float, y: float) -> bool:
        if self.heapStruct == TSConstants.BinaryHeap.min:
            return x < y
        elif self.heapStruct == TSConstants.BinaryHeap.max:
            return x > y

    def _getSwapChild(self, node: TSBinaryHeapNode) -> Union[TSBinaryHeapNode, None]:
        if not node.leftChildNode and not node.rightChildNode:
            return None
        elif node.leftChildNode and not node.rightChildNode:
            if self.heapStruct == TSConstants.BinaryHeap.min:
                if node.order > node.leftChildNode.order:
                    return node.leftChildNode
                else:
                    return None
            elif self.heapStruct == TSConstants.BinaryHeap.max:
                if node.order < node.leftChildNode.order:
                    return node.leftChildNode
                else:
                    return None
        elif not node.leftChildNode and node.rightChildNode:
            if self.heapStruct == TSConstants.BinaryHeap.min:
                if node.order > node.rightChildNode.order:
                    return node.rightChildNode
                else:
                    return None
            elif self.heapStruct == TSConstants.BinaryHeap.max:
                if node.order < node.rightChildNode.order:
                    return node.rightChildNode
                else:
                    return None
        else:
            if self.heapStruct == TSConstants.BinaryHeap.min:
                if node.leftChildNode.order < node.rightChildNode.order:
                    if node.order > node.leftChildNode.order:
                        return node.leftChildNode
                    else:
                        return None
                else:
                    if node.order > node.rightChildNode.order:
                        return node.rightChildNode
                    else:
                        return None
            elif self.heapStruct == TSConstants.BinaryHeap.max:
                if node.leftChildNode.order > node.rightChildNode.order:
                    if node.order < node.leftChildNode.order:
                        return node.leftChildNode
                    else:
                        return None
                else:
                    if node.order < node.rightChildNode.order:
                        return node.rightChildNode
                    else:
                        return None

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

                if node.parentNode:
                    if node.parentNode.leftChildNode == parentNode:
                        node.parentNode.leftChildNode = node
                    else:
                        node.parentNode.rightChildNode = node

                parentIndex = ceil(node.index / 2) - 1
                parentNode = node.parentNode

    def deleteNodeByOrder(self, order: float):
        deleteNode = self.getNodeByOrder(order)
        if deleteNode:
            self._deleteNodeInDictByOrder(order)
            node = self.heapList[-1]
            if len(self.heapList) == 1:
                deleteNode.index = -1
                self.heapList.pop()
                return
            elif node == deleteNode:
                if deleteNode.parentNode.rightChildNode == deleteNode:
                    deleteNode.parentNode.rightChildNode = None
                else:
                    deleteNode.parentNode.leftChildNode = None
                deleteNode.parentNode = None
                deleteNode.index = -1
                self.heapList.pop()
                return
            elif deleteNode.index == ceil(node.index / 2) - 1:
                self.heapList[deleteNode.index], self.heapList[node.index] = \
                    self.heapList[node.index], self.heapList[deleteNode.index]

                node.index = deleteNode.index

                if deleteNode.leftChildNode == node:
                    node.rightChildNode = deleteNode.rightChildNode
                    node.leftChildNode = None
                    if node.rightChildNode:
                        node.rightChildNode.parentNode = node
                else:
                    node.leftChildNode = deleteNode.leftChildNode
                    node.rightChildNode = None
                    if node.leftChildNode:
                        node.leftChildNode.parentNode = node

                node.parentNode = deleteNode.parentNode
                if node.parentNode:
                    if node.parentNode.leftChildNode == deleteNode:
                        node.parentNode.leftChildNode = node
                    else:
                        node.parentNode.rightChildNode = node
            else:
                self.heapList[deleteNode.index], self.heapList[node.index] = \
                    self.heapList[node.index], self.heapList[deleteNode.index]

                node.index = deleteNode.index

                if node.parentNode.leftChildNode == node:
                    node.parentNode.leftChildNode = None
                else:
                    node.parentNode.rightChildNode = None
                node.parentNode = deleteNode.parentNode
                node.leftChildNode = deleteNode.leftChildNode
                node.rightChildNode = deleteNode.rightChildNode
                if node.parentNode:
                    if node.parentNode.leftChildNode == deleteNode:
                        node.parentNode.leftChildNode = node
                    else:
                        node.parentNode.rightChildNode = node
                if node.leftChildNode:
                    node.leftChildNode.parentNode = node
                if node.rightChildNode:
                    node.rightChildNode.parentNode = node

            deleteNode.parentNode = None
            deleteNode.leftChildNode = None
            deleteNode.rightChildNode = None
            deleteNode.index = -1
            self.heapList.pop()

            if node.parentNode and self._compare(node.order, node.parentNode.order):
                parentIndex = ceil(node.index / 2) - 1
                parentNode = self.heapList[parentIndex]
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

                    if node.parentNode:
                        if node.parentNode.leftChildNode == parentNode:
                            node.parentNode.leftChildNode = node
                        else:
                            node.parentNode.rightChildNode = node

                    parentIndex = ceil(node.index / 2) - 1
                    parentNode = node.parentNode
            else:
                childNode = self._getSwapChild(node)
                while childNode:
                    self.heapList[childNode.index], self.heapList[node.index] = \
                        self.heapList[node.index], self.heapList[childNode.index]

                    childNode.index, node.index = node.index, childNode.index

                    if node.leftChildNode == childNode:
                        childNode.rightChildNode, node.rightChildNode = node.rightChildNode, childNode.rightChildNode
                        node.leftChildNode = childNode.leftChildNode
                        childNode.leftChildNode = node
                        if childNode.rightChildNode:
                            childNode.rightChildNode.parentNode = childNode
                        if node.rightChildNode:
                            node.rightChildNode.parentNode = node
                        if node.leftChildNode:
                            node.leftChildNode.parentNode = node
                    else:
                        childNode.leftChildNode, node.leftChildNode = node.leftChildNode, childNode.leftChildNode
                        node.rightChildNode = childNode.rightChildNode
                        childNode.rightChildNode = node
                        if childNode.leftChildNode:
                            childNode.leftChildNode.parentNode = childNode
                        if node.leftChildNode:
                            node.leftChildNode.parentNode = node
                        if node.rightChildNode:
                            node.rightChildNode.parentNode = node

                    childNode.parentNode = node.parentNode
                    node.parentNode = childNode

                    if childNode.parentNode:
                        if childNode.parentNode.leftChildNode == node:
                            childNode.parentNode.leftChildNode = childNode
                        else:
                            childNode.parentNode.rightChildNode = childNode

                    childNode = self._getSwapChild(node)

    def getNodeByOrder(self, order: float) -> Union[TSBinaryHeapNode, None]:
        return self.heapDict.get(order, [None])[0]

    def getTreeHeight(self) -> int:
        nodeCount = len(self.heapList)
        if not nodeCount:
            return -1
        return floor(log2(nodeCount))

    def getTreeNodeCount(self) -> int:
        return len(self.heapList)
