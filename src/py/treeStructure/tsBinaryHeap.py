from .tsBinaryHeapNode import TSBinaryHeapNode
from .tsConstants import TSConstants
from typing import Union, Deque, List
from collections import deque
from math import ceil, floor, log2
import random


class TSBinaryHeap:
    def __init__(self, node: Union[TSBinaryHeapNode, None] = None, heapStruct: str = TSConstants.BinaryHeap.min):
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

    def _deleteNodeInDictByOrder(self, order: Union[float, int]):
        if order in self.heapDict:
            self.heapDict[order].popleft()
            if not len(self.heapDict[order]):
                del self.heapDict[order]

    def _compare(self, x: Union[float, int], y: Union[float, int]) -> bool:
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

    def _swapUp(self, node: TSBinaryHeapNode):
        parentNode = node.parentNode
        while parentNode and self._compare(node.order, parentNode.order):
            self.heapList[parentNode.index], self.heapList[node.index] = \
                self.heapList[node.index], self.heapList[parentNode.index]

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

            parentNode = node.parentNode

    def _swapDown(self, node: TSBinaryHeapNode):
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

    def insertNode(self, node: TSBinaryHeapNode):
        self.heapList.append(node)
        self._appendNodeIntoDict(node)
        node.index = len(self.heapList) - 1
        if not node.index:
            node.parentNode = None
        else:
            node.parentNode = self.heapList[ceil(node.index / 2) - 1]
            if node.index % 2:
                node.parentNode.leftChildNode = node
            else:
                node.parentNode.rightChildNode = node
            self._swapUp(node)

    def deleteNodeByOrder(self, order: Union[float, int]):
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
                self._swapUp(node)
            else:
                self._swapDown(node)

    def getNodeByOrder(self, order: Union[float, int]) -> Union[TSBinaryHeapNode, None]:
        return self.heapDict.get(order, [None])[0]

    def getTreeHeight(self) -> int:
        nodeCount = len(self.heapList)
        if not nodeCount:
            return -1
        return floor(log2(nodeCount))

    def getTreeNodeCount(self) -> int:
        return len(self.heapList)

    def getOrderedList(self, onlyOrder: bool = False) -> List[Union[TSBinaryHeapNode, float, int]]:
        returnList: Deque[Union[TSBinaryHeapNode, float, int]] = deque()
        length = len(self.heapList)
        if self.heapStruct == TSConstants.BinaryHeap.max:
            for n in self.heapList:
                returnList.append(n)
            for i in range(length - 1):
                # Swap max and last element in tree
                returnList[0], returnList[length - i - 1] = returnList[length - i - 1], returnList[0]
                if onlyOrder:
                    returnList[length - i - 1] = returnList[length - i - 1].order
                currentIdx = 0
                while currentIdx * 2 + 1 <= length - i - 2:
                    #  Check right child exist
                    if currentIdx * 2 + 2 <= length - i - 2:
                        if returnList[currentIdx * 2 + 1].order >= returnList[currentIdx * 2 + 2].order:
                            maxChildNodeIdx = currentIdx * 2 + 1
                        else:
                            maxChildNodeIdx = currentIdx * 2 + 2
                    else:
                        maxChildNodeIdx = currentIdx * 2 + 1
                    # No need to swap if current is greater than children
                    if returnList[maxChildNodeIdx].order <= returnList[currentIdx].order:
                        break
                    else:
                        returnList[maxChildNodeIdx], returnList[currentIdx] = returnList[currentIdx], returnList[
                            maxChildNodeIdx]
                        currentIdx = maxChildNodeIdx
        else:
            for n in self.heapList:
                returnList.appendleft(n)
            for i in range(length - 1):
                # Swap min and first element in tree
                returnList[-1], returnList[i] = returnList[i], returnList[-1]
                if onlyOrder:
                    returnList[i] = returnList[i].order
                currentIdx = length - 1
                while currentIdx * 2 - length >= i + 1:
                    #  Check right child exist
                    if currentIdx * 2 - length - 1 >= i + 1:
                        if returnList[currentIdx * 2 - length].order <= returnList[currentIdx * 2 - length - 1].order:
                            minChildNodeIdx = currentIdx * 2 - length
                        else:
                            minChildNodeIdx = currentIdx * 2 - length - 1
                    else:
                        minChildNodeIdx = currentIdx * 2 - length
                    # No need to swap if current is smaller than children
                    if returnList[minChildNodeIdx].order >= returnList[currentIdx].order:
                        break
                    else:
                        returnList[minChildNodeIdx], returnList[currentIdx] = returnList[currentIdx], returnList[
                            minChildNodeIdx]
                        currentIdx = minChildNodeIdx
        return list(returnList)

    def getRankByOrder(self, order: Union[float, int]) -> int:
        node = self.getNodeByOrder(order)
        if node:
            smallerNodeCount = 0
            for n in self.heapList:
                if n.order < node.order:
                    smallerNodeCount += 1
            return smallerNodeCount
        else:
            return -1

    def getNodeByRank(self, rank: int) -> Union[TSBinaryHeapNode, None]:
        if rank < 0 or rank > len(self.heapList):
            return None
        return self._getNodeByRank(list(self.heapList), rank)

    def _getNodeByRank(self, array: List[TSBinaryHeapNode], rank: int) -> Union[TSBinaryHeapNode, None]:
        if not array:
            return None
        pivotNode = random.choice(array)
        smallerNode = []
        equalNode = []
        biggerNode = []
        for node in array:
            if pivotNode.order > node.order:
                smallerNode.append(node)
            elif pivotNode.order == node.order:
                equalNode.append(node)
            else:
                biggerNode.append(node)
        lenOfSmallerNode = len(smallerNode)
        lenOfEqualNode = len(equalNode)
        if rank < lenOfSmallerNode:
            return self._getNodeByRank(smallerNode, rank)
        elif rank >= lenOfSmallerNode + lenOfEqualNode:
            return self._getNodeByRank(biggerNode, rank - lenOfSmallerNode - lenOfEqualNode)
        else:
            return equalNode[0]

    def deleteMaxOrderNode(self):
        if self.heapList:
            if self.heapStruct == TSConstants.BinaryHeap.max:
                self.deleteNodeByOrder(self.heapList[0].order)
            elif self.heapStruct == TSConstants.BinaryHeap.min:
                maxNode = self.getMaxOrderNode()
                if maxNode:
                    self.deleteNodeByOrder(maxNode.order)

    def deleteMinOrderNode(self):
        if self.heapList:
            if self.heapStruct == TSConstants.BinaryHeap.min:
                self.deleteNodeByOrder(self.heapList[0].order)
            elif self.heapStruct == TSConstants.BinaryHeap.max:
                minNode = self.getMinOrderNode()
                if minNode:
                    self.deleteNodeByOrder(minNode.order)

    def getMaxOrderNode(self) -> Union[TSBinaryHeapNode, None]:
        if not self.heapList:
            return None
        else:
            if self.heapStruct == TSConstants.BinaryHeap.min:
                return max(self.heapList[floor(len(self.heapList) / 2):], key=lambda node: node.order)
            elif self.heapStruct == TSConstants.BinaryHeap.max:
                return self.heapList[0]

    def getMinOrderNode(self) -> Union[TSBinaryHeapNode, None]:
        if not self.heapList:
            return None
        else:
            if self.heapStruct == TSConstants.BinaryHeap.max:
                return min(self.heapList[floor(len(self.heapList) / 2):], key=lambda node: node.order)
            elif self.heapStruct == TSConstants.BinaryHeap.min:
                return self.heapList[0]

    def beautifulPrint(self, onlyOrder: bool = False) -> Union[dict, list, None]:
        if self.heapList:
            return self._beautifulPrint(self.heapList[0], onlyOrder)
        else:
            if onlyOrder:
                return [None]
            else:
                return None

    def _beautifulPrint(self, node: Union[TSBinaryHeapNode, None], onlyOrder: bool = False) -> Union[dict, list, None]:
        if not node:
            if onlyOrder:
                return [None]
            else:
                return None
        else:
            if onlyOrder:
                return [
                    node.order,
                    self._beautifulPrint(node.leftChildNode, onlyOrder),
                    self._beautifulPrint(node.rightChildNode, onlyOrder)
                ]
            else:
                return {
                    TSConstants.BinaryNode.order: node.order,
                    TSConstants.BinaryNode.value: node.value,
                    TSConstants.BinaryNode.leftChildNode: self._beautifulPrint(node.leftChildNode),
                    TSConstants.BinaryNode.rightChildNode: self._beautifulPrint(node.rightChildNode)
                }

    def changeHeapStruct(self):
        if self.heapStruct == TSConstants.BinaryHeap.max:
            self.heapStruct = TSConstants.BinaryHeap.min
        elif self.heapStruct == TSConstants.BinaryHeap.min:
            self.heapStruct = TSConstants.BinaryHeap.max
        if len(self.heapList) > 1:
            for index in range(floor(len(self.heapList) / 2) - 1, -1, -1):
                self._swapDown(self.heapList[index])

    def mergeWithOtherTree(self, tree: 'TSBinaryHeap'):
        if len(self.heapList) >= len(tree.heapList):
            # Merge dict
            for key in tree.heapDict.keys():
                if key in self.heapDict:
                    self.heapDict[key] += tree.heapDict[key]
                else:
                    self.heapDict[key] = tree.heapDict[key]
            tree.heapDict = self.heapDict
            # Merge list
            for node in tree.heapList:
                self.heapList.append(node)
                node.index = len(self.heapList) - 1
                parentNode = self.heapList[ceil(node.index / 2) - 1]
                if parentNode.leftChildNode:
                    parentNode.rightChildNode = node
                else:
                    parentNode.leftChildNode = node
                node.parentNode = parentNode
                node.leftChildNode = None
                node.rightChildNode = None
            if len(self.heapList) > 1:
                for index in range(floor(len(self.heapList) / 2) - 1, -1, -1):
                    self._swapDown(self.heapList[index])
            tree.heapList = self.heapList
            tree.heapStruct = self.heapStruct
        else:
            tree.mergeWithOtherTree(self)
