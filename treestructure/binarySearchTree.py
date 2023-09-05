"""
Module of binary search tree.
"""

from .binaryNode import BinaryNode
from typing import Union, List
from .constants import Constants
from collections import deque


class BinarySearchTree:

    def __init__(self, node: Union[BinaryNode, None] = None):
        """
        Module of binary search tree.

        :param node: Root node of tree.
        """

        self._checkNodeConnection(node)
        self._rootNode: Union[BinaryNode, None] = node
        if node:
            node._inTree = True

    @property
    def rootNode(self) -> Union[BinaryNode, None]:
        return self._rootNode

    def _checkNodeConnection(self, node: Union[BinaryNode, None] = None):
        """
        Check whether node is already in another tree.

        :param node: Binary node to check.
        :return: None.
        """

        if node:
            if node._inTree:
                raise Exception('Node is already in other tree')

    def insertNode(self, node: BinaryNode):
        """
        Insert node into tree.

        :param node: node that will be joined.
        :return: None.
        """

        self._checkNodeConnection(node)
        node._inTree = True
        if not self._rootNode:
            self._rootNode = node
        else:
            iterNode = self._rootNode
            while iterNode:
                if iterNode._order > node._order:
                    if iterNode._leftChildNode:
                        iterNode = iterNode._leftChildNode
                    else:
                        iterNode._leftChildNode = node
                        iterNode._leftChildNode._parentNode = iterNode
                        break
                else:
                    if iterNode._rightChildNode:
                        iterNode = iterNode._rightChildNode
                    else:
                        iterNode._rightChildNode = node
                        iterNode._rightChildNode._parentNode = iterNode
                        break

    def deleteNode(self, order: Union[float, int]) -> Union[BinaryNode, None]:
        """
        Delete node by order.

        :param order: Delete a node with giving order.
        :return: The node that be removed. Return None if there's no node with giving order.
        """

        if not self._rootNode:
            return None
        else:
            iterNode = self._rootNode
            while iterNode:
                if iterNode._order == order:
                    if not iterNode._leftChildNode and not iterNode._rightChildNode:
                        if iterNode._parentNode:
                            if iterNode._parentNode._leftChildNode == iterNode:
                                iterNode._parentNode._leftChildNode = None
                            else:
                                iterNode._parentNode._rightChildNode = None
                        else:
                            self._rootNode = None
                    elif iterNode._leftChildNode and not iterNode._rightChildNode:
                        if iterNode._parentNode:
                            if iterNode._parentNode._leftChildNode == iterNode:
                                iterNode._parentNode._leftChildNode = iterNode._leftChildNode
                            else:
                                iterNode._parentNode._rightChildNode = iterNode._leftChildNode
                        else:
                            self._rootNode = iterNode._leftChildNode
                        iterNode._leftChildNode._parentNode = iterNode._parentNode
                    elif not iterNode._leftChildNode and iterNode._rightChildNode:
                        if iterNode._parentNode:
                            if iterNode._parentNode._leftChildNode == iterNode:
                                iterNode._parentNode._leftChildNode = iterNode._rightChildNode
                            else:
                                iterNode._parentNode._rightChildNode = iterNode._rightChildNode
                        else:
                            self._rootNode = iterNode._rightChildNode
                        iterNode._rightChildNode._parentNode = iterNode._parentNode
                    else:
                        maxNodeInLeft = iterNode._leftChildNode
                        if not maxNodeInLeft._rightChildNode:
                            if iterNode._parentNode:
                                if iterNode._parentNode._leftChildNode == iterNode:
                                    iterNode._parentNode._leftChildNode = maxNodeInLeft
                                else:
                                    iterNode._parentNode._rightChildNode = maxNodeInLeft
                            else:
                                self._rootNode = maxNodeInLeft
                            maxNodeInLeft._parentNode = iterNode._parentNode
                            maxNodeInLeft._rightChildNode = iterNode._rightChildNode
                            iterNode._rightChildNode._parentNode = maxNodeInLeft
                        else:
                            while maxNodeInLeft:
                                if maxNodeInLeft._rightChildNode:
                                    maxNodeInLeft = maxNodeInLeft._rightChildNode
                                else:
                                    break

                            maxNodeInLeft._parentNode._rightChildNode = maxNodeInLeft._leftChildNode
                            if maxNodeInLeft._leftChildNode:
                                maxNodeInLeft._leftChildNode._parentNode = maxNodeInLeft._parentNode

                            if iterNode._parentNode:
                                if iterNode._parentNode._leftChildNode == iterNode:
                                    iterNode._parentNode._leftChildNode = maxNodeInLeft
                                else:
                                    iterNode._parentNode._rightChildNode = maxNodeInLeft
                            else:
                                self._rootNode = maxNodeInLeft
                            maxNodeInLeft._parentNode = iterNode._parentNode
                            maxNodeInLeft._leftChildNode = iterNode._leftChildNode
                            maxNodeInLeft._rightChildNode = iterNode._rightChildNode
                            iterNode._leftChildNode._parentNode = maxNodeInLeft
                            iterNode._rightChildNode._parentNode = maxNodeInLeft
                    iterNode._leftChildNode = None
                    iterNode._rightChildNode = None
                    iterNode._parentNode = None
                    iterNode._inTree = False
                    return iterNode
                elif iterNode._order > order:
                    if iterNode._leftChildNode:
                        iterNode = iterNode._leftChildNode
                    else:
                        return None
                else:
                    if iterNode._rightChildNode:
                        iterNode = iterNode._rightChildNode
                    else:
                        return None

    def height(self) -> int:
        """
        Tree height.

        If there's no node in tree, height is -1.

        If there's only one node in tree, height is 0.

        :return: Tree height.
        """

        return self._height(self._rootNode)

    def _height(self, rootNode: Union[BinaryNode, None]) -> int:
        """
        Tree height with specific root node.

        If root node is None, height is -1.

        If root node does not have ant child, height is 0.

        :param rootNode: Root node of tree.
        :return: Tree height.
        """

        height = -1
        if not rootNode:
            return height
        q = deque()
        q.append(rootNode)
        while len(q):
            height += 1
            for i in range(len(q)):
                node = q.popleft()
                if node._leftChildNode:
                    q.append(node._leftChildNode)
                if node._rightChildNode:
                    q.append(node._rightChildNode)
        return height

    def nodeCount(self) -> int:
        """
        Calculate how many nodes are in tree.

        :return: Nodes number in tree.
        """

        return self._nodeCount(self._rootNode)

    def _nodeCount(self, rootNode: Union[BinaryNode, None]) -> int:
        """
        Calculate how many nodes are in tree with specific root node.

        :param rootNode: Root node of tree.
        :return: Nodes number in tree.
        """

        count = 0
        if not rootNode:
            return count
        q = deque()
        q.append(rootNode)
        while len(q):
            count += len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node._leftChildNode:
                    q.append(node._leftChildNode)
                if node._rightChildNode:
                    q.append(node._rightChildNode)
        return count

    def orderedList(self, onlyOrder: bool = False) -> List[Union[BinaryNode, float, int]]:
        """
        Sort node by order.

        :param onlyOrder: Return array only contains order if onlyOrder is True. Default is False.
        :return: Sorted list.
        """

        return self._orderedList(self._rootNode, onlyOrder)

    def _orderedList(self, rootNode: Union[BinaryNode, None], onlyOrder: bool = False) -> List[
        Union[BinaryNode, float, int]]:
        """
        Sort node by order with specific root node.

        :param rootNode: Root node of tree.
        :param onlyOrder: Return array only contains order if onlyOrder is True. Default is False.
        :return: Sorted list.
        """

        orderedList = []
        if not rootNode:
            return orderedList
        stk = deque()
        node = rootNode
        while node or len(stk):
            while node:
                stk.append(node)
                node = node._leftChildNode
            node = stk.pop();
            if onlyOrder:
                orderedList.append(node._order);
            else:
                orderedList.append(node)
            node = node._rightChildNode;
        return orderedList

    def getNodeByOrder(self, order: Union[float, int]) -> Union[BinaryNode, None]:
        """
        Search a node with giving order.

        :param order: Node order.
        :return: Node with giving order. Return None if there's no node with giving order.
        """

        if not self._rootNode:
            return None
        else:
            iterNode = self._rootNode
            while iterNode:
                if iterNode._order == order:
                    while iterNode._leftChildNode:
                        if iterNode._leftChildNode._order == order:
                            iterNode = iterNode._leftChildNode
                        else:
                            break
                    return iterNode
                elif iterNode._order > order:
                    iterNode = iterNode._leftChildNode
                else:
                    iterNode = iterNode._rightChildNode
            return None

    def getRankByOrder(self, order: Union[float, int]) -> int:
        """
        Check the rank of node in sorted list with specific order. Rank start with 0.

        If there's no node with giving order. Rank is -1.

        :param order: Node order.
        :return: Rank of node in sorted list. Return -1 if there's no node with giving order.
        """

        node = self.getNodeByOrder(order)
        if not node:
            return -1
        else:
            rank = self._nodeCount(node._leftChildNode) + 1
            iterNode = node
            while iterNode._parentNode:
                if iterNode._parentNode._rightChildNode == iterNode:
                    rank += self._nodeCount(iterNode._parentNode._leftChildNode) + 1
                iterNode = iterNode._parentNode
            return rank - 1

    def getNodeByRank(self, rank: int) -> Union[BinaryNode, None]:
        """
        Get node by giving rank in sorted list.

        :param rank: Rank in sorted list.
        :return: Node in tree. Return None if rank < 0 or rank >= node count.
        """

        if rank < 0:
            return None
        stk = deque()
        node = self._rootNode
        while node or len(stk):
            while node:
                stk.append(node)
                node = node._leftChildNode
            node = stk.pop()
            rank -= 1
            if rank < 0:
                return node
            node = node._rightChildNode
        return None

    def maxNode(self) -> Union[BinaryNode, None]:
        """
        Get max order node in tree.

        :return: Max order node in tree. Return None if tree is empty.
        """

        if not self._rootNode:
            return None
        else:
            iterNode = self._rootNode
            while iterNode:
                if iterNode._rightChildNode:
                    iterNode = iterNode._rightChildNode
                else:
                    return iterNode

    def minNode(self) -> Union[BinaryNode, None]:
        """
        Get min order node in tree.

        :return: Min order node in tree. Return None if tree is empty.
        """

        if not self._rootNode:
            return None
        else:
            iterNode = self._rootNode
            while iterNode:
                if iterNode._leftChildNode:
                    iterNode = iterNode._leftChildNode
                else:
                    return iterNode

    def deleteMaxNode(self) -> Union[BinaryNode, None]:
        """
        Delete max order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        node = self.maxNode()
        if node:
            if node._parentNode:
                node._parentNode._rightChildNode = node._leftChildNode
            else:
                self._rootNode = node._leftChildNode
            if node._leftChildNode:
                node._leftChildNode._parentNode = node._parentNode
            node._leftChildNode = None
            node._parentNode = None
            node._inTree = False
        return node

    def deleteMinNode(self) -> Union[BinaryNode, None]:
        """
        Delete min order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        node = self.minNode()
        if node:
            if node._parentNode:
                node._parentNode._leftChildNode = node._rightChildNode
            else:
                self._rootNode = node._rightChildNode
            if node._rightChildNode:
                node._rightChildNode._parentNode = node._parentNode
            node._rightChildNode = None
            node._parentNode = None
            node._inTree = False
        return node

    def package(self, onlyOrder: bool = False) -> Union[dict, list, None]:
        """
        Package tree structure and return.

        :param onlyOrder: Return tree only contains order in each node if onlyOrder is True. Default is False.
        :return: Tree structure as dictionary. Return type is list if onlyOrder is True. Return None if tree is empty.
        """

        return self._package(self._rootNode, onlyOrder)

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

    def balance(self):
        """
        Make tree balance.

        :return: None.
        """

        orderedList = self.orderedList()
        if len(orderedList) > 2:
            self._rootNode = self._balance(orderedList)

    def _balance(self, orderedList: List[BinaryNode]) -> BinaryNode:
        """
        Balance tree.

        :param orderedList: List of node.
        :return: None.
        """

        if len(orderedList) == 1:
            orderedList[0]._parentNode = None
            orderedList[0]._leftChildNode = None
            orderedList[0]._rightChildNode = None
            return orderedList[0]
        elif len(orderedList) == 2:
            orderedList[0]._parentNode = orderedList[1]
            orderedList[0]._leftChildNode = None
            orderedList[0]._rightChildNode = None
            orderedList[1]._parentNode = None
            orderedList[1]._leftChildNode = orderedList[0]
            orderedList[1]._rightChildNode = None
            return orderedList[1]
        else:
            centerIndex = len(orderedList) // 2
            centerNode = orderedList[centerIndex]
            leftNode = self._balance(orderedList[:centerIndex])
            rightNode = self._balance(orderedList[centerIndex + 1:])
            centerNode._parentNode = None
            centerNode._leftChildNode = leftNode
            centerNode._rightChildNode = rightNode
            leftNode._parentNode = centerNode
            rightNode._parentNode = centerNode
            return centerNode

    def merge(self, tree: 'BinarySearchTree'):
        """
        Merge two trees.

        :param tree: Tree that will be merged.
        :return: None.
        """

        l1 = self.orderedList()
        l2 = tree.orderedList()
        orderedList = []
        while l1 and l2:
            if l1[0]._order >= l2[0]._order:
                orderedList.append(l2[0])
                del l2[0]
            else:
                orderedList.append(l1[0])
                del l1[0]
        if l1:
            orderedList = orderedList + l1
        elif l2:
            orderedList = orderedList + l2
        self._rootNode = self._balance(orderedList)
        tree._rootNode = None

    def clear(self):
        """
        Clear tree.

        :return: None.
        """

        if self._rootNode:
            q = deque()
            q.append(self._rootNode)
            while len(q):
                for i in range(len(q)):
                    node = q.popleft()
                    if node._leftChildNode:
                        q.append(node._leftChildNode)
                    if node._rightChildNode:
                        q.append(node._rightChildNode)
                    node._parentNode = None
                    node._leftChildNode = None
                    node._rightChildNode = None
                    node._inTree = False
        self._rootNode = None
