"""
Implementation of basic binary search tree.
"""

from .binaryNode import BinaryNode
from typing import Union, List
from .constants import Constants
from collections import deque


class BinarySearchTree:

    def __init__(self, node: Union[BinaryNode, None] = None):
        """
        Basic binary search tree.

        :param node: Root node of tree.
        """

        self._checkNodeConnection(node)
        self.rootNode: Union[BinaryNode, None] = node

    def _checkNodeConnection(self, node: Union[BinaryNode, None] = None):
        """
        Check whether node is already in another tree.

        :param node: Binary node to check.
        :return: None.
        """

        if node:
            if node.parentNode or node.leftChildNode or node.rightChildNode:
                raise Exception('Node is already in other tree')

    def insertNode(self, node: BinaryNode):
        """
        Insert node into tree.

        :param node: node that will be joined.
        :return: None.
        """

        self._checkNodeConnection(node)
        if not self.rootNode:
            self.rootNode = node
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.order > node.order:
                    if iterNode.leftChildNode:
                        iterNode = iterNode.leftChildNode
                    else:
                        iterNode.leftChildNode = node
                        iterNode.leftChildNode.parentNode = iterNode
                        break
                else:
                    if iterNode.rightChildNode:
                        iterNode = iterNode.rightChildNode
                    else:
                        iterNode.rightChildNode = node
                        iterNode.rightChildNode.parentNode = iterNode
                        break

    def deleteNode(self, order: Union[float, int]) -> Union[BinaryNode, None]:
        """
        Delete node by order.

        :param order: Delete a node with same order.
        :return: The node that be removed. Return None if there's no node with same order.
        """

        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.order == order:
                    if not iterNode.leftChildNode and not iterNode.rightChildNode:
                        if iterNode.parentNode:
                            if iterNode.parentNode.leftChildNode == iterNode:
                                iterNode.parentNode.leftChildNode = None
                            else:
                                iterNode.parentNode.rightChildNode = None
                        else:
                            self.rootNode = None
                    elif iterNode.leftChildNode and not iterNode.rightChildNode:
                        if iterNode.parentNode:
                            if iterNode.parentNode.leftChildNode == iterNode:
                                iterNode.parentNode.leftChildNode = iterNode.leftChildNode
                            else:
                                iterNode.parentNode.rightChildNode = iterNode.leftChildNode
                        else:
                            self.rootNode = iterNode.leftChildNode
                        iterNode.leftChildNode.parentNode = iterNode.parentNode
                    elif not iterNode.leftChildNode and iterNode.rightChildNode:
                        if iterNode.parentNode:
                            if iterNode.parentNode.leftChildNode == iterNode:
                                iterNode.parentNode.leftChildNode = iterNode.rightChildNode
                            else:
                                iterNode.parentNode.rightChildNode = iterNode.rightChildNode
                        else:
                            self.rootNode = iterNode.rightChildNode
                        iterNode.rightChildNode.parentNode = iterNode.parentNode
                    else:
                        maxNodeInLeft = iterNode.leftChildNode
                        if not maxNodeInLeft.rightChildNode:
                            if iterNode.parentNode:
                                if iterNode.parentNode.leftChildNode == iterNode:
                                    iterNode.parentNode.leftChildNode = maxNodeInLeft
                                else:
                                    iterNode.parentNode.rightChildNode = maxNodeInLeft
                            else:
                                self.rootNode = maxNodeInLeft
                            maxNodeInLeft.parentNode = iterNode.parentNode
                            maxNodeInLeft.rightChildNode = iterNode.rightChildNode
                            iterNode.rightChildNode.parentNode = maxNodeInLeft
                        else:
                            while maxNodeInLeft:
                                if maxNodeInLeft.rightChildNode:
                                    maxNodeInLeft = maxNodeInLeft.rightChildNode
                                else:
                                    break

                            maxNodeInLeft.parentNode.rightChildNode = maxNodeInLeft.leftChildNode
                            if maxNodeInLeft.leftChildNode:
                                maxNodeInLeft.leftChildNode.parentNode = maxNodeInLeft.parentNode

                            if iterNode.parentNode:
                                if iterNode.parentNode.leftChildNode == iterNode:
                                    iterNode.parentNode.leftChildNode = maxNodeInLeft
                                else:
                                    iterNode.parentNode.rightChildNode = maxNodeInLeft
                            else:
                                self.rootNode = maxNodeInLeft
                            maxNodeInLeft.parentNode = iterNode.parentNode
                            maxNodeInLeft.leftChildNode = iterNode.leftChildNode
                            maxNodeInLeft.rightChildNode = iterNode.rightChildNode
                            iterNode.leftChildNode.parentNode = maxNodeInLeft
                            iterNode.rightChildNode.parentNode = maxNodeInLeft
                    iterNode.leftChildNode = None
                    iterNode.rightChildNode = None
                    iterNode.parentNode = None
                    return iterNode
                elif iterNode.order > order:
                    if iterNode.leftChildNode:
                        iterNode = iterNode.leftChildNode
                    else:
                        return None
                else:
                    if iterNode.rightChildNode:
                        iterNode = iterNode.rightChildNode
                    else:
                        return None

    def height(self) -> int:
        """
        Tree height.

        If there's no node in tree, height is -1.

        If there's only one node in tree, height is 0.

        :return: Tree height.
        """

        height = -1
        if not self.rootNode:
            return height
        q = deque()
        q.append(self.rootNode)
        while len(q):
            height += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                if node.rightChildNode:
                    q.append(node.rightChildNode)
        return height

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
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                if node.rightChildNode:
                    q.append(node.rightChildNode)
        return height

    def nodeCount(self) -> int:
        """
        Calculate how many nodes in tree.

        :return: Nodes number in tree.
        """

        count = 0
        if not self.rootNode:
            return count
        q = deque()
        q.append(self.rootNode)
        while len(q):
            count += len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                if node.rightChildNode:
                    q.append(node.rightChildNode)
        return count

    def _nodeCount(self, rootNode: Union[BinaryNode, None]) -> int:
        """
        Calculate how many nodes in tree with specific root node.

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
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                if node.rightChildNode:
                    q.append(node.rightChildNode)
        return count

    def orderedList(self, onlyOrder: bool = False) -> List[Union[BinaryNode, float, int]]:
        """
        Sort node by order.

        :param onlyOrder: Return array only contains order if onlyOrder is True. Default is False.
        :return: Sorted list.
        """

        orderedList = []
        if not self.rootNode:
            return orderedList
        stk = deque()
        node = self.rootNode
        while node or len(stk):
            while node:
                stk.append(node)
                node = node.leftChildNode
            node = stk.pop();
            if onlyOrder:
                orderedList.append(node.order);
            else:
                orderedList.append(node)
            node = node.rightChildNode
        return orderedList

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
                node = node.leftChildNode
            node = stk.pop();
            if onlyOrder:
                orderedList.append(node.order);
            else:
                orderedList.append(node)
            node = node.rightChildNode;
        return orderedList

    def getNodeByOrder(self, order: Union[float, int]) -> Union[BinaryNode, None]:
        """
        Search node by giving order.

        :param order: Find node with same order.
        :return: Node with same order. Return None if there's no node with same order.
        """

        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.order == order:
                    while iterNode.leftChildNode:
                        if iterNode.leftChildNode.order == order:
                            iterNode = iterNode.leftChildNode
                        else:
                            break
                    return iterNode
                elif iterNode.order > order:
                    iterNode = iterNode.leftChildNode
                else:
                    iterNode = iterNode.rightChildNode
            return None

    def getRankByOrder(self, order: Union[float, int]) -> int:
        """
        Check the rank of node in sorted list with specific order. Rank start with 0.

        If there's no node with same order. Rank is -1.

        :param order: Node order.
        :return: Rank of node in sorted list. Return -1 if there's no node with same order.
        """

        node = self.getNodeByOrder(order)
        if not node:
            return -1
        else:
            rank = self._nodeCount(node.leftChildNode) + 1
            iterNode = node
            while iterNode.parentNode:
                if iterNode.parentNode.rightChildNode == iterNode:
                    rank += self._nodeCount(iterNode.parentNode.leftChildNode) + 1
                iterNode = iterNode.parentNode
            return rank - 1

    def getNodeByRank(self, rank: int) -> Union[BinaryNode, None]:
        """
        Get node by rank in sorted list.

        :param rank: Rank in sorted list.
        :return: Node in tree. Return None if rank < 0 or rank >= node count.
        """

        if rank < 0:
            return None
        node = self.rootNode
        while node:
            leftCount = self._nodeCount(node.leftChildNode)
            if leftCount == rank:
                return node
            elif leftCount < rank:
                rank = rank - leftCount - 1
                node = node.rightChildNode
            else:
                node = node.leftChildNode
        return None

    def maxNode(self) -> Union[BinaryNode, None]:
        """
        Get max node in tree.

        :return: Max node in tree.
        """

        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.rightChildNode:
                    iterNode = iterNode.rightChildNode
                else:
                    return iterNode

    def minNode(self) -> Union[BinaryNode, None]:
        """
        Get min order node in tree.

        :return: Min order node in tree.
        """

        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.leftChildNode:
                    iterNode = iterNode.leftChildNode
                else:
                    return iterNode

    def deleteMaxNode(self) -> Union[BinaryNode, None]:
        """
        Delete max order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        node = self.maxNode()
        if node:
            if node.parentNode:
                node.parentNode.rightChildNode = node.leftChildNode
            else:
                self.rootNode = node.leftChildNode
            if node.leftChildNode:
                node.leftChildNode.parentNode = node.parentNode
            node.leftChildNode = None
            node.parentNode = None
        return node

    def deleteMinNode(self) -> Union[BinaryNode, None]:
        """
        Delete min order node in tree.

        :return: The node that be removed. Return None if there's no node in tree.
        """

        node = self.minNode()
        if node:
            if node.parentNode:
                node.parentNode.leftChildNode = node.rightChildNode
            else:
                self.rootNode = node.rightChildNode
            if node.rightChildNode:
                node.rightChildNode.parentNode = node.parentNode
            node.rightChildNode = None
            node.parentNode = None
        return node

    def package(self, onlyOrder: bool = False) -> Union[dict, list, None]:
        """
        Package tree structure and return.

        :param onlyOrder: Return tree only contains order in each node if onlyOrder is True. Default is False.
        :return: Tree structure as dictionary. Return type is list if onlyOrder is True. Return None if tree is empty.
        """

        return self._package(self.rootNode, onlyOrder)

    def _package(self, node: Union[BinaryNode, None], onlyOrder: bool = False) -> Union[dict, list, None]:
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

    def balance(self):
        """
        Balance tree.

        :return: None.
        """

        orderedList = self.orderedList()
        if len(orderedList) > 2:
            self.rootNode = self._balance(orderedList)

    def _balance(self, orderedList: List[BinaryNode]) -> BinaryNode:
        """
        Balance tree.

        :param orderedList: List of node.
        :return: None.
        """

        if len(orderedList) == 1:
            orderedList[0].parentNode = None
            orderedList[0].leftChildNode = None
            orderedList[0].rightChildNode = None
            return orderedList[0]
        elif len(orderedList) == 2:
            orderedList[0].parentNode = orderedList[1]
            orderedList[0].leftChildNode = None
            orderedList[0].rightChildNode = None
            orderedList[1].parentNode = None
            orderedList[1].leftChildNode = orderedList[0]
            orderedList[1].rightChildNode = None
            return orderedList[1]
        else:
            centerIndex = len(orderedList) // 2
            centerNode = orderedList[centerIndex]
            leftNode = self._balance(orderedList[:centerIndex])
            rightNode = self._balance(orderedList[centerIndex + 1:])
            centerNode.parentNode = None
            centerNode.leftChildNode = leftNode
            centerNode.rightChildNode = rightNode
            leftNode.parentNode = centerNode
            rightNode.parentNode = centerNode
            return centerNode

    def merge(self, tree: 'BinarySearchTree'):
        """
        Merge two tree.

        :param tree: Tree will be merged.
        :return: None.
        """

        l1 = self.orderedList()
        l2 = tree.orderedList()
        orderedList = []
        while l1 and l2:
            if l1[0].order >= l2[0].order:
                orderedList.append(l2[0])
                del l2[0]
            else:
                orderedList.append(l1[0])
                del l1[0]
        if l1:
            orderedList = orderedList + l1
        elif l2:
            orderedList = orderedList + l2
        self.rootNode = self._balance(orderedList)
        tree.rootNode = self.rootNode

    def clear(self):
        """
        Clear tree.

        :return: None.
        """

        if self.rootNode:
            q = deque()
            q.append(self.rootNode)
            while len(q):
                for i in range(len(q)):
                    node = q.popleft()
                    if node.leftChildNode:
                        q.append(node.leftChildNode)
                    if node.rightChildNode:
                        q.append(node.rightChildNode)
                    node.parentNode = None
                    node.leftChildNode = None
                    node.rightChildNode = None
        self.rootNode = None
