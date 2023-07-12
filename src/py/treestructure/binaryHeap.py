"""
Implementation of binary heap.

I do some improve to reduce searching node time complexity from O(n) to O(1).
"""

from .binaryHeapNode import BinaryHeapNode
from .constants import Constants
from typing import Union, Deque, List
from collections import deque
from itertools import islice
from random import choice


class BinaryHeap:
    def __init__(self, node: Union[BinaryHeapNode, None] = None, heapStruct: str = Constants.BinaryHeap.min):
        """
        Basic binary heap.

        :param node: Root node of tree.
        :param heapStruct: Determine the struct of heap. It can be 'min' or 'max'.
        """

        if heapStruct != Constants.BinaryHeap.min and heapStruct != Constants.BinaryHeap.max:
            raise Exception('Heap struct can only be min or max')
        self.heapStruct = heapStruct
        self.heapList: Deque[BinaryHeapNode] = deque()
        self.heapDict = {}
        if node:
            self._checkNodeConnection(node)
            self.heapList.append(node)
            self.heapDict[node.order] = deque([node])
            node.index = 0

    def _checkNodeConnection(self, node: Union[BinaryHeapNode, None] = None):
        """
        Check whether node is already in another tree.

        :param node: Heap node to check.
        :return: None.
        """

        if node:
            if node.parentNode or node.leftChildNode or node.rightChildNode:
                raise Exception('Node is already in other tree')

    def _appendNodeIntoDict(self, node: BinaryHeapNode):
        """
        Append heap node into dictionary.

        :param node: Heap node that will be inserted.
        :return: None.
        """

        if node.order in self.heapDict:
            self.heapDict[node.order].append(node)
        else:
            self.heapDict[node.order] = deque([node])

    def _deleteNodeInDictByOrder(self, order: Union[float, int]):
        """
        Delete heap node from dictionary.

        :param order: Delete a node with same order.
        :return: None.
        """

        if order in self.heapDict:
            self.heapDict[order].popleft()
            if not len(self.heapDict[order]):
                del self.heapDict[order]

    def _compare(self, x: Union[float, int], y: Union[float, int]) -> bool:
        """
        Compare two numbers by heap struct.

        :param x: Number.
        :param y: Number.
        :return: Boolean.
        """

        if self.heapStruct == Constants.BinaryHeap.min:
            return x < y
        elif self.heapStruct == Constants.BinaryHeap.max:
            return x > y

    def _getSwapChild(self, node: BinaryHeapNode) -> Union[BinaryHeapNode, None]:
        """
        Get child node to swap.

        :param node: Node to swap.
        :return: Child node to swap. Return None if swapping is not necessary.
        """

        if not node.leftChildNode and not node.rightChildNode:
            return None
        elif node.leftChildNode and not node.rightChildNode:
            if self.heapStruct == Constants.BinaryHeap.min:
                if node.order > node.leftChildNode.order:
                    return node.leftChildNode
                else:
                    return None
            elif self.heapStruct == Constants.BinaryHeap.max:
                if node.order < node.leftChildNode.order:
                    return node.leftChildNode
                else:
                    return None
        elif not node.leftChildNode and node.rightChildNode:
            if self.heapStruct == Constants.BinaryHeap.min:
                if node.order > node.rightChildNode.order:
                    return node.rightChildNode
                else:
                    return None
            elif self.heapStruct == Constants.BinaryHeap.max:
                if node.order < node.rightChildNode.order:
                    return node.rightChildNode
                else:
                    return None
        else:
            if self.heapStruct == Constants.BinaryHeap.min:
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
            elif self.heapStruct == Constants.BinaryHeap.max:
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

    def _swapUp(self, node: BinaryHeapNode):
        """
        Swap up with parent node.

        :param node: Node to swap.
        :return: None.
        """

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

    def _swapDown(self, node: BinaryHeapNode):
        """
        Swap down with children node.

        :param node: Node to swap.
        :return: None.
        """

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

    def insertNode(self, node: BinaryHeapNode):
        """
        Insert node into tree.

        :param node: node that will be joined.
        :return: None.
        """

        self._checkNodeConnection(node)
        self.heapList.append(node)
        self._appendNodeIntoDict(node)
        node.index = len(self.heapList) - 1
        if node.index:
            node.parentNode = self.heapList[-(node.index // -2) - 1]
            if node.index % 2:
                node.parentNode.leftChildNode = node
            else:
                node.parentNode.rightChildNode = node
            self._swapUp(node)

    def deleteNode(self, order: Union[float, int]) -> Union[BinaryHeapNode, None]:
        """
        Delete node by order.

        :param order: Delete a node with same order.
        :return: The node that be removed. Return None if there's no node with same order.
        """

        deleteNode = self.getNodeByOrder(order)
        if deleteNode:
            self._deleteNodeInDictByOrder(order)
            node = self.heapList[-1]
            if len(self.heapList) == 1:
                deleteNode.index = -1
                self.heapList.pop()
                return deleteNode
            elif node == deleteNode:
                if deleteNode.parentNode.rightChildNode == deleteNode:
                    deleteNode.parentNode.rightChildNode = None
                else:
                    deleteNode.parentNode.leftChildNode = None
                deleteNode.parentNode = None
                deleteNode.index = -1
                self.heapList.pop()
                return deleteNode
            elif deleteNode.index == -(node.index // -2) - 1:
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
        return deleteNode

    def height(self) -> int:
        """
        Tree height.

        If there's no node in tree, height is -1.

        If there's only one node in tree, height is 0.

        :return: Tree height.
        """

        nodeCount = len(self.heapList)
        if not nodeCount:
            return -1
        return len(bin(nodeCount)) - 3

    def nodeCount(self) -> int:
        """
        Calculate how many nodes in tree.

        :return: Nodes number in tree.
        """

        return len(self.heapList)

    def orderedList(self, onlyOrder: bool = False) -> List[Union[BinaryHeapNode, float, int]]:
        """
        Sort node by order.

        :param onlyOrder: Return array only contains order if onlyOrder is True. Default is False.
        :return: Sorted list.
        """

        returnList: Deque[Union[BinaryHeapNode, float, int]] = deque()
        length = len(self.heapList)
        if self.heapStruct == Constants.BinaryHeap.max:
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
            if onlyOrder:
                returnList[0] = returnList[0].order
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
            if onlyOrder:
                returnList[-1] = returnList[-1].order
        return list(returnList)

    def getNodeByOrder(self, order: Union[float, int]) -> Union[BinaryHeapNode, None]:
        """
        Search node by giving order.

        :param order: Find node with same order.
        :return: Node with same order. Return None if there's no node with same order.
        """

        return self.heapDict.get(order, [None])[0]

    def getRankByOrder(self, order: Union[float, int]) -> int:
        """
        Check the rank of node in sorted list with specific order. Rank start with 0.

        If there's no node with same order. Rank is -1.

        :param order: Node order.
        :return: Rank of node in sorted list. Return -1 if there's no node with same order.
        """

        node = self.getNodeByOrder(order)
        if node:
            smallerNodeCount = 0
            for n in self.heapList:
                if n.order < node.order:
                    smallerNodeCount += 1
            return smallerNodeCount
        else:
            return -1

    def getNodeByRank(self, rank: int) -> Union[BinaryHeapNode, None]:
        """
        Get node by rank in sorted list.

        :param rank: Rank in sorted list.
        :return: Node in tree. Return None if rank < 0 or rank >= node count.
        """

        if rank < 0 or rank > len(self.heapList):
            return None
        return self._getNodeByRank(self.heapList, rank)

    def _getNodeByRank(self, array: Deque[BinaryHeapNode], rank: int) -> Union[BinaryHeapNode, None]:
        """
        Get node by rank in sorted list with specific tree.

        :param array: Heap tree.
        :param rank: Rank in sorted list.
        :return: Node in tree. Return None tree is empty.
        """

        if not array:
            return None
        pivotNode = choice(array)
        smallerNode = deque()
        equalNode = deque()
        biggerNode = deque()
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

    def maxNode(self) -> Union[BinaryHeapNode, None]:
        """
        Get max node in tree.

        :return: Max node in tree.
        """

        if not self.heapList:
            return None
        else:
            if self.heapStruct == Constants.BinaryHeap.min:
                return max(islice(self.heapList, len(self.heapList) // 2, None), key=lambda node: node.order)
            elif self.heapStruct == Constants.BinaryHeap.max:
                return self.heapList[0]

    def minNode(self) -> Union[BinaryHeapNode, None]:
        """
        Get min order node in tree.

        :return: Min order node in tree.
        """

        if not self.heapList:
            return None
        else:
            if self.heapStruct == Constants.BinaryHeap.max:
                return min(islice(self.heapList, len(self.heapList) // 2, None), key=lambda node: node.order)
            elif self.heapStruct == Constants.BinaryHeap.min:
                return self.heapList[0]

    def deleteMaxNode(self):
        """
        Delete max order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        if self.heapList:
            if self.heapStruct == Constants.BinaryHeap.max:
                self.deleteNode(self.heapList[0].order)
            elif self.heapStruct == Constants.BinaryHeap.min:
                maxNode = self.maxNode()
                if maxNode:
                    self.deleteNode(maxNode.order)

    def deleteMinNode(self):
        """
        Delete min order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        if self.heapList:
            if self.heapStruct == Constants.BinaryHeap.min:
                self.deleteNode(self.heapList[0].order)
            elif self.heapStruct == Constants.BinaryHeap.max:
                minNode = self.minNode()
                if minNode:
                    self.deleteNode(minNode.order)

    def package(self, onlyOrder: bool = False) -> Union[dict, list, None]:
        """
        Package tree structure and return.

        :param onlyOrder: Return tree only contains order in each node if onlyOrder is True. Default is False.
        :return: Tree structure as dictionary. Return type is list if onlyOrder is True. Return None if tree is empty.
        """

        if self.heapList:
            return self._package(self.heapList[0], onlyOrder)
        else:
            if onlyOrder:
                return [None]
            else:
                return None

    def _package(self, node: Union[BinaryHeapNode, None], onlyOrder: bool = False) -> Union[dict, list, None]:
        """
        Package tree structure and return.

        :param node: Root node of tree.
        :param onlyOrder: Return tree only contains order in each node if onlyOrder is True. Default is False.
        :return: Tree structure as dictionary. Return type is list if onlyOrder is True. Return None if tree is empty.
        """

        if not node:
            if onlyOrder:
                return [None]
            else:
                return None
        else:
            if onlyOrder:
                return [
                    node.order,
                    self._package(node.leftChildNode, onlyOrder),
                    self._package(node.rightChildNode, onlyOrder)
                ]
            else:
                return {
                    Constants.BinaryNode.order: node.order,
                    Constants.BinaryNode.value: node.value,
                    Constants.BinaryNode.leftChildNode: self._package(node.leftChildNode),
                    Constants.BinaryNode.rightChildNode: self._package(node.rightChildNode)
                }

    def transform(self):
        """
        Transform from min heap to max heap/max heap to min heap.

        :return: None.
        """

        if self.heapStruct == Constants.BinaryHeap.max:
            self.heapStruct = Constants.BinaryHeap.min
        elif self.heapStruct == Constants.BinaryHeap.min:
            self.heapStruct = Constants.BinaryHeap.max
        if len(self.heapList) > 1:
            for index in range(len(self.heapList) // 2 - 1, -1, -1):
                self._swapDown(self.heapList[index])

    def merge(self, tree: 'BinaryHeap'):
        """
        Merge two tree.

        Heap struct of merged tree is equal to the tree that node count is smaller.

        :param tree: Tree will be merged.
        :return: None.
        """

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
                parentNode = self.heapList[-(node.index // -2) - 1]
                if parentNode.leftChildNode:
                    parentNode.rightChildNode = node
                else:
                    parentNode.leftChildNode = node
                node.parentNode = parentNode
                node.leftChildNode = None
                node.rightChildNode = None
            if len(self.heapList) > 1:
                for index in range(len(self.heapList) // 2 - 1, -1, -1):
                    self._swapDown(self.heapList[index])
            tree.heapList = self.heapList
            tree.heapStruct = self.heapStruct
        else:
            tree.merge(self)

    def clear(self):
        """
        Clear tree.

        :return: None.
        """
        for node in self.heapList:
            node.parentNode = None
            node.leftChildNode = None
            node.rightChildNode = None
        self.heapDict.clear()
        self.heapList.clear()
