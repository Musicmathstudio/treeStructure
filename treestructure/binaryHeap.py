"""
Module of binary heap.

I make some improvement to reduce time complexity of searching node from O(n) to O(1).
"""

from .binaryNode import BinaryNode
from .constants import Constants
from typing import Union, Deque, List
from collections import deque
from itertools import islice
from random import choice


class BinaryHeap:
    def __init__(self, node: Union[BinaryNode, None] = None, heapStruct: str = Constants.BinaryHeap.min):
        """
        Module of binary heap.

        :param node: Root node of tree.
        :param heapStruct: It defines the structure of tree should be min heap or max heap.
        It can be 'min' or 'max'.
        Default struct is min heap.
        """

        if heapStruct != Constants.BinaryHeap.min and heapStruct != Constants.BinaryHeap.max:
            raise Exception('Heap struct can only be min or max')
        self._heapStruct = heapStruct
        self._heapList: Deque[BinaryNode] = deque()
        # Store node into a hashtable for increasing searching time.
        self._heapDict = {}
        if node:
            self._checkNodeConnection(node)
            self._heapList.append(node)
            self._heapDict[node._order] = deque([node])
            node._index = 0
            node._inTree = True

    @property
    def heapStruct(self) -> str:
        return self._heapStruct

    def _checkNodeConnection(self, node: Union[BinaryNode, None] = None):
        """
        Check whether node is already in another tree.

        :param node: Heap node to check.
        :return: None.
        """

        if node:
            if node._inTree:
                raise Exception('Node is already in other tree')

    def _appendNodeIntoDict(self, node: BinaryNode):
        """
        Append heap node into dictionary.

        :param node: Heap node that will be inserted.
        :return: None.
        """

        if node._order in self._heapDict:
            self._heapDict[node._order].append(node)
        else:
            self._heapDict[node._order] = deque([node])

    def _deleteNodeInDictByOrder(self, order: Union[float, int]):
        """
        Delete heap node from dictionary.

        :param order: Node order.
        :return: None.
        """

        if order in self._heapDict:
            self._heapDict[order].popleft()
            if not len(self._heapDict[order]):
                del self._heapDict[order]

    def _compare(self, x: Union[float, int], y: Union[float, int]) -> bool:
        """
        Compare two numbers by heap struct.

        :param x: Number.
        :param y: Number.
        :return: Boolean.
        """

        if self._heapStruct == Constants.BinaryHeap.min:
            return x < y
        elif self._heapStruct == Constants.BinaryHeap.max:
            return x > y

    def _getSwapChild(self, node: BinaryNode) -> Union[BinaryNode, None]:
        """
        Get child node to swap.

        :param node: Node to swap.
        :return: Child node to swap. Return None if swapping is not necessary.
        """

        if not node._leftChildNode and not node._rightChildNode:
            return None
        elif node._leftChildNode and not node._rightChildNode:
            if self._heapStruct == Constants.BinaryHeap.min:
                if node._order > node._leftChildNode._order:
                    return node._leftChildNode
                else:
                    return None
            elif self._heapStruct == Constants.BinaryHeap.max:
                if node._order < node._leftChildNode._order:
                    return node._leftChildNode
                else:
                    return None
        elif not node._leftChildNode and node._rightChildNode:
            if self._heapStruct == Constants.BinaryHeap.min:
                if node._order > node._rightChildNode._order:
                    return node._rightChildNode
                else:
                    return None
            elif self._heapStruct == Constants.BinaryHeap.max:
                if node._order < node._rightChildNode._order:
                    return node._rightChildNode
                else:
                    return None
        else:
            if self._heapStruct == Constants.BinaryHeap.min:
                if node._leftChildNode._order < node._rightChildNode._order:
                    if node._order > node._leftChildNode._order:
                        return node._leftChildNode
                    else:
                        return None
                else:
                    if node._order > node._rightChildNode._order:
                        return node._rightChildNode
                    else:
                        return None
            elif self._heapStruct == Constants.BinaryHeap.max:
                if node._leftChildNode._order > node._rightChildNode._order:
                    if node._order < node._leftChildNode._order:
                        return node._leftChildNode
                    else:
                        return None
                else:
                    if node._order < node._rightChildNode._order:
                        return node._rightChildNode
                    else:
                        return None

    def _swapUp(self, node: BinaryNode):
        """
        Swap up with parent node.

        :param node: Node to swap.
        :return: None.
        """

        parentNode = node._parentNode
        while parentNode and self._compare(node._order, parentNode._order):
            self._heapList[parentNode._index], self._heapList[node._index] = \
                self._heapList[node._index], self._heapList[parentNode._index]

            parentNode._index, node._index = node._index, parentNode._index

            if parentNode._leftChildNode == node:
                node._rightChildNode, parentNode._rightChildNode = parentNode._rightChildNode, node._rightChildNode
                parentNode._leftChildNode = node._leftChildNode
                node._leftChildNode = parentNode
                if node._rightChildNode:
                    node._rightChildNode._parentNode = node
                if parentNode._rightChildNode:
                    parentNode._rightChildNode._parentNode = parentNode
                if parentNode._leftChildNode:
                    parentNode._leftChildNode._parentNode = parentNode
            else:
                node._leftChildNode, parentNode._leftChildNode = parentNode._leftChildNode, node._leftChildNode
                parentNode._rightChildNode = node._rightChildNode
                node._rightChildNode = parentNode
                if node._leftChildNode:
                    node._leftChildNode._parentNode = node
                if parentNode._leftChildNode:
                    parentNode._leftChildNode._parentNode = parentNode
                if parentNode._rightChildNode:
                    parentNode._rightChildNode._parentNode = parentNode

            node._parentNode = parentNode._parentNode
            parentNode._parentNode = node

            if node._parentNode:
                if node._parentNode._leftChildNode == parentNode:
                    node._parentNode._leftChildNode = node
                else:
                    node._parentNode._rightChildNode = node

            parentNode = node._parentNode

    def _swapDown(self, node: BinaryNode):
        """
        Swap down with children node.

        :param node: Node to swap.
        :return: None.
        """

        childNode = self._getSwapChild(node)
        while childNode:
            self._heapList[childNode._index], self._heapList[node._index] = \
                self._heapList[node._index], self._heapList[childNode._index]

            childNode._index, node._index = node._index, childNode._index

            if node._leftChildNode == childNode:
                childNode._rightChildNode, node._rightChildNode = node._rightChildNode, childNode._rightChildNode
                node._leftChildNode = childNode._leftChildNode
                childNode._leftChildNode = node
                if childNode._rightChildNode:
                    childNode._rightChildNode._parentNode = childNode
                if node._rightChildNode:
                    node._rightChildNode._parentNode = node
                if node._leftChildNode:
                    node._leftChildNode._parentNode = node
            else:
                childNode._leftChildNode, node._leftChildNode = node._leftChildNode, childNode._leftChildNode
                node._rightChildNode = childNode._rightChildNode
                childNode._rightChildNode = node
                if childNode._leftChildNode:
                    childNode._leftChildNode._parentNode = childNode
                if node._leftChildNode:
                    node._leftChildNode._parentNode = node
                if node._rightChildNode:
                    node._rightChildNode._parentNode = node

            childNode._parentNode = node._parentNode
            node._parentNode = childNode

            if childNode._parentNode:
                if childNode._parentNode._leftChildNode == node:
                    childNode._parentNode._leftChildNode = childNode
                else:
                    childNode._parentNode._rightChildNode = childNode

            childNode = self._getSwapChild(node)

    def insertNode(self, node: BinaryNode):
        """
        Insert node into tree.

        :param node: node that will be joined.
        :return: None.
        """

        self._checkNodeConnection(node)
        node._inTree = True
        if self._heapList and node == self._heapList[0]:
            raise Exception('Node is already in other tree')
        self._heapList.append(node)
        self._appendNodeIntoDict(node)
        node._index = len(self._heapList) - 1
        if node._index:
            node._parentNode = self._heapList[-(node._index // -2) - 1]
            if node._index % 2:
                node._parentNode._leftChildNode = node
            else:
                node._parentNode._rightChildNode = node
            self._swapUp(node)

    def deleteNode(self, order: Union[float, int]) -> Union[BinaryNode, None]:
        """
        Delete node by order.

        :param order: Node order.
        :return: The node that be removed. Return None if there's no node with giving order.
        """

        deleteNode = self.getNodeByOrder(order)
        if deleteNode:
            self._deleteNodeInDictByOrder(order)
            node = self._heapList[-1]
            if len(self._heapList) == 1:
                deleteNode._index = -1
                self._heapList.pop()
                return deleteNode
            elif node == deleteNode:
                if deleteNode._parentNode._rightChildNode == deleteNode:
                    deleteNode._parentNode._rightChildNode = None
                else:
                    deleteNode._parentNode._leftChildNode = None
                deleteNode._parentNode = None
                deleteNode._index = -1
                self._heapList.pop()
                return deleteNode
            elif deleteNode._index == -(node._index // -2) - 1:
                self._heapList[deleteNode._index], self._heapList[node._index] = \
                    self._heapList[node._index], self._heapList[deleteNode._index]

                node._index = deleteNode._index

                if deleteNode._leftChildNode == node:
                    node._rightChildNode = deleteNode._rightChildNode
                    node._leftChildNode = None
                    if node._rightChildNode:
                        node._rightChildNode._parentNode = node
                else:
                    node._leftChildNode = deleteNode._leftChildNode
                    node._rightChildNode = None
                    if node._leftChildNode:
                        node._leftChildNode._parentNode = node

                node._parentNode = deleteNode._parentNode

                if node._parentNode:
                    if node._parentNode._leftChildNode == deleteNode:
                        node._parentNode._leftChildNode = node
                    else:
                        node._parentNode._rightChildNode = node
            else:
                self._heapList[deleteNode._index], self._heapList[node._index] = \
                    self._heapList[node._index], self._heapList[deleteNode._index]

                node._index = deleteNode._index

                if node._parentNode._leftChildNode == node:
                    node._parentNode._leftChildNode = None
                else:
                    node._parentNode._rightChildNode = None
                node._parentNode = deleteNode._parentNode
                node._leftChildNode = deleteNode._leftChildNode
                node._rightChildNode = deleteNode._rightChildNode
                if node._parentNode:
                    if node._parentNode._leftChildNode == deleteNode:
                        node._parentNode._leftChildNode = node
                    else:
                        node._parentNode._rightChildNode = node
                if node._leftChildNode:
                    node._leftChildNode._parentNode = node
                if node._rightChildNode:
                    node._rightChildNode._parentNode = node

            deleteNode._parentNode = None
            deleteNode._leftChildNode = None
            deleteNode._rightChildNode = None
            deleteNode._index = -1
            deleteNode._inTree = False
            self._heapList.pop()

            if node._parentNode and self._compare(node._order, node._parentNode._order):
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

        nodeCount = len(self._heapList)
        if not nodeCount:
            return -1
        return len(bin(nodeCount)) - 3

    def nodeCount(self) -> int:
        """
        Calculate how many nodes are in tree.

        :return: Nodes number in tree.
        """

        return len(self._heapList)

    def orderedList(self, onlyOrder: bool = False) -> List[Union[BinaryNode, float, int]]:
        """
        Sort node by order.

        :param onlyOrder: Return array only contains order if onlyOrder is True. Default is False.
        :return: Sorted list.
        """

        returnList = self._heapList.copy()
        length = len(self._heapList)
        if self._heapStruct == Constants.BinaryHeap.max:
            for i in range(length - 1):
                # Swap max and last element in tree
                returnList[0], returnList[length - i - 1] = returnList[length - i - 1], returnList[0]
                if onlyOrder:
                    returnList[length - i - 1] = returnList[length - i - 1]._order
                currentIdx = 0
                while currentIdx * 2 + 1 <= length - i - 2:
                    #  Check right child exist
                    if currentIdx * 2 + 2 <= length - i - 2:
                        if returnList[currentIdx * 2 + 1]._order >= returnList[currentIdx * 2 + 2]._order:
                            maxChildNodeIdx = currentIdx * 2 + 1
                        else:
                            maxChildNodeIdx = currentIdx * 2 + 2
                    else:
                        maxChildNodeIdx = currentIdx * 2 + 1
                    # No need to swap if current is greater than children
                    if returnList[maxChildNodeIdx]._order <= returnList[currentIdx]._order:
                        break
                    else:
                        returnList[maxChildNodeIdx], returnList[currentIdx] = returnList[currentIdx], returnList[
                            maxChildNodeIdx]
                        currentIdx = maxChildNodeIdx
            if onlyOrder:
                returnList[0] = returnList[0]._order
        elif self._heapStruct == Constants.BinaryHeap.min:
            returnList.reverse()
            for i in range(length - 1):
                # Swap min and first element in tree
                returnList[-1], returnList[i] = returnList[i], returnList[-1]
                if onlyOrder:
                    returnList[i] = returnList[i]._order
                currentIdx = length - 1
                while currentIdx * 2 - length >= i + 1:
                    #  Check right child exist
                    if currentIdx * 2 - length - 1 >= i + 1:
                        if returnList[currentIdx * 2 - length]._order <= returnList[currentIdx * 2 - length - 1]._order:
                            minChildNodeIdx = currentIdx * 2 - length
                        else:
                            minChildNodeIdx = currentIdx * 2 - length - 1
                    else:
                        minChildNodeIdx = currentIdx * 2 - length
                    # No need to swap if current is smaller than children
                    if returnList[minChildNodeIdx]._order >= returnList[currentIdx]._order:
                        break
                    else:
                        returnList[minChildNodeIdx], returnList[currentIdx] = returnList[currentIdx], returnList[
                            minChildNodeIdx]
                        currentIdx = minChildNodeIdx
            if onlyOrder:
                returnList[-1] = returnList[-1]._order
        return list(returnList)

    def getNodeByOrder(self, order: Union[float, int]) -> Union[BinaryNode, None]:
        """
        Search a node with giving order.

        :param order: Node order.
        :return: Node with giving order. Return None if there's no node with giving order.
        """

        return self._heapDict.get(order, [None])[0]

    def getRankByOrder(self, order: Union[float, int]) -> int:
        """
        Check the rank of node in sorted list with specific order. Rank start with 0.

        If there's no node with giving order. Rank is -1.

        :param order: Node order.
        :return: Rank of node in sorted list. Return -1 if there's no node with giving order.
        """

        node = self.getNodeByOrder(order)
        if node:
            smallerNodeCount = 0
            for n in self._heapList:
                if n._order < node._order:
                    smallerNodeCount += 1
            return smallerNodeCount
        else:
            return -1

    def getNodeByRank(self, rank: int) -> Union[BinaryNode, None]:
        """
        Get node by giving rank in sorted list.

        :param rank: Rank in sorted list.
        :return: Node in tree. Return None if rank < 0 or rank >= node count.
        """

        if rank < 0 or rank > len(self._heapList):
            return None
        return self._getNodeByRank(self._heapList, rank)

    def _getNodeByRank(self, array: Deque[BinaryNode], rank: int) -> Union[BinaryNode, None]:
        """
        Get node by giving rank in sorted list with specific tree.

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
            if pivotNode._order > node._order:
                smallerNode.append(node)
            elif pivotNode._order == node._order:
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

    def maxNode(self) -> Union[BinaryNode, None]:
        """
        Get max order node in tree.

        :return: Max order node in tree. Return None if tree is empty.
        """

        if not self._heapList:
            return None
        else:
            if self._heapStruct == Constants.BinaryHeap.min:
                return max(islice(self._heapList, len(self._heapList) // 2, None), key=lambda node: node._order)
            elif self._heapStruct == Constants.BinaryHeap.max:
                return self._heapList[0]

    def minNode(self) -> Union[BinaryNode, None]:
        """
        Get min order node in tree.

        :return: Min order node in tree. Return None if tree is empty.
        """

        if not self._heapList:
            return None
        else:
            if self._heapStruct == Constants.BinaryHeap.max:
                return min(islice(self._heapList, len(self._heapList) // 2, None), key=lambda node: node._order)
            elif self._heapStruct == Constants.BinaryHeap.min:
                return self._heapList[0]

    def deleteMaxNode(self) -> Union[BinaryNode, None]:
        """
        Delete max order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        if self._heapList:
            if self._heapStruct == Constants.BinaryHeap.max:
                return self.deleteNode(self._heapList[0]._order)
            elif self._heapStruct == Constants.BinaryHeap.min:
                maxNode = self.maxNode()
                if maxNode:
                    return self.deleteNode(maxNode._order)

    def deleteMinNode(self) -> Union[BinaryNode, None]:
        """
        Delete min order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        if self._heapList:
            if self._heapStruct == Constants.BinaryHeap.min:
                return self.deleteNode(self._heapList[0]._order)
            elif self._heapStruct == Constants.BinaryHeap.max:
                minNode = self.minNode()
                if minNode:
                    return self.deleteNode(minNode._order)

    def package(self, onlyOrder: bool = False) -> Union[dict, list, None]:
        """
        Package tree structure and return.

        :param onlyOrder: Return tree only contains order in each node if onlyOrder is True. Default is False.
        :return: Tree structure as dictionary. Return type is list if onlyOrder is True. Return None if tree is empty.
        Return [None] if tree is empty and onlyOrder is True.
        """

        if self._heapList:
            return self._package(self._heapList[0], onlyOrder)
        else:
            if onlyOrder:
                return [None]
            else:
                return None

    def _package(self, node: Union[BinaryNode, None], onlyOrder: bool = False) -> Union[dict, list, None]:
        """
        Package tree structure and return.

        :param node: Root node of tree.
        :param onlyOrder: Return tree only contains order in each node if onlyOrder is True. Default is False.
        :return: Tree structure as dictionary. Return type is list if onlyOrder is True. Return None if tree is empty.
        Return [None] if tree is empty and onlyOrder is True.
        """

        if not node:
            if onlyOrder:
                return [None]
            else:
                return None
        else:
            if onlyOrder:
                return [
                    node._order,
                    self._package(node._leftChildNode, onlyOrder),
                    self._package(node._rightChildNode, onlyOrder)
                ]
            else:
                return {
                    Constants.BinaryNode.order: node._order,
                    Constants.BinaryNode.value: node._value,
                    Constants.BinaryNode.leftChildNode: self._package(node._leftChildNode),
                    Constants.BinaryNode.rightChildNode: self._package(node._rightChildNode)
                }

    def transform(self):
        """
        Transform heap struct from min heap to max heap/max heap to min heap.

        :return: None.
        """

        if self._heapStruct == Constants.BinaryHeap.max:
            self._heapStruct = Constants.BinaryHeap.min
        elif self._heapStruct == Constants.BinaryHeap.min:
            self._heapStruct = Constants.BinaryHeap.max
        if len(self._heapList) > 1:
            for index in range(len(self._heapList) // 2 - 1, -1, -1):
                self._swapDown(self._heapList[index])

    def merge(self, tree: 'BinaryHeap'):
        """
        Merge two trees.

        :param tree: Tree that will be merged.
        :return: None.
        """

        # Merge dict
        for key in tree._heapDict.keys():
            if key in self._heapDict:
                self._heapDict[key] += tree._heapDict[key]
            else:
                self._heapDict[key] = tree._heapDict[key]
        # Merge list
        for node in tree._heapList:
            self._heapList.append(node)
            node._index = len(self._heapList) - 1
            parentNode = self._heapList[-(node._index // -2) - 1]
            if parentNode._leftChildNode:
                parentNode._rightChildNode = node
            else:
                parentNode._leftChildNode = node
            node._parentNode = parentNode
            node._leftChildNode = None
            node._rightChildNode = None
        if len(self._heapList) > 1:
            for index in range(len(self._heapList) // 2 - 1, -1, -1):
                self._swapDown(self._heapList[index])
        tree._heapList.clear()
        tree._heapDict.clear()

    def clear(self):
        """
        Clear tree.

        :return: None.
        """

        for node in self._heapList:
            node._parentNode = None
            node._leftChildNode = None
            node._rightChildNode = None
            node._index = -1
            node._inTree = False
        self._heapDict.clear()
        self._heapList.clear()
