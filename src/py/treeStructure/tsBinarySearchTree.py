from .tsBinaryNode import TSBinaryNode
from typing import Union, List
from .tsConstants import TSConstants
from collections import deque


class TSBinarySearchTree:

    def __init__(self, node: Union[TSBinaryNode, None] = None):
        self.rootNode: Union[TSBinaryNode, None] = node
        if self.rootNode:
            self.rootNode.parentNode = None

    def insertNode(self, node: TSBinaryNode):
        if not self.rootNode:
            self.rootNode = node
            self.rootNode.parentNode = None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.order >= node.order:
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

    def deleteNodeByOrder(self, order: float):
        if not self.rootNode:
            return
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
                    iterNode.leftChildNode = None
                    iterNode.rightChildNode = None
                    iterNode.parentNode = None
                    break
                elif iterNode.order >= order:
                    if iterNode.leftChildNode:
                        iterNode = iterNode.leftChildNode
                    else:
                        break
                else:
                    if iterNode.rightChildNode:
                        iterNode = iterNode.rightChildNode
                    else:
                        break

    def getNodeByOrder(self, order: float) -> Union[TSBinaryNode, None]:
        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.order == order:
                    return iterNode
                elif iterNode.order >= order:
                    iterNode = iterNode.leftChildNode
                else:
                    iterNode = iterNode.rightChildNode
            return None

    def getTreeHeight(self) -> int:
        height = -1
        if not self.rootNode:
            return height
        q = deque()
        q.append(self.rootNode)
        size = 1
        while size:
            height += 1
            for i in range(size):
                node = q.popleft()
                size -= 1
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                    size += 1
                if node.rightChildNode:
                    q.append(node.rightChildNode)
                    size += 1
        return height

    def _getTreeHeight(self, rootNode: Union[TSBinaryNode, None]) -> int:
        height = -1
        if not rootNode:
            return height
        q = deque()
        q.append(rootNode)
        size = 1
        while size:
            height += 1
            for i in range(size):
                node = q.popleft()
                size -= 1
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                    size += 1
                if node.rightChildNode:
                    q.append(node.rightChildNode)
                    size += 1
        return height

    def getTreeNodeCount(self) -> int:
        count = 0
        if not self.rootNode:
            return count
        q = deque()
        q.append(self.rootNode)
        size = 1
        while size:
            count += size
            for i in range(size):
                node = q.popleft()
                size -= 1
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                    size += 1
                if node.rightChildNode:
                    q.append(node.rightChildNode)
                    size += 1
        return count

    def _getTreeNodeCount(self, rootNode: Union[TSBinaryNode, None]) -> int:
        count = 0
        if not rootNode:
            return count
        q = deque()
        q.append(rootNode)
        size = 1
        while size:
            count += size
            for i in range(size):
                node = q.popleft()
                size -= 1
                if node.leftChildNode:
                    q.append(node.leftChildNode)
                    size += 1
                if node.rightChildNode:
                    q.append(node.rightChildNode)
                    size += 1
        return count

    def getOrderedList(self) -> List[TSBinaryNode]:
        orderedList = []
        if not self.rootNode:
            return orderedList
        stk = deque()
        size = 0
        node = self.rootNode
        while node or size:
            while node:
                stk.append(node)
                size += 1
                node = node.leftChildNode
            node = stk.pop();
            size -= 1
            orderedList.append(node);
            node = node.rightChildNode;
        return orderedList

    def _getOrderedList(self, rootNode: Union[TSBinaryNode, None]) -> List[TSBinaryNode]:
        orderedList = []
        if not rootNode:
            return orderedList
        stk = deque()
        size = 0
        node = rootNode
        while node or size:
            while node:
                stk.append(node)
                size += 1
                node = node.leftChildNode
            node = stk.pop();
            size -= 1
            orderedList.append(node);
            node = node.rightChildNode;
        return orderedList

    def getRankByOrder(self, order: float) -> int:
        node = self.getNodeByOrder(order)
        if not node:
            return -1
        else:
            rank = self._getTreeNodeCount(node.leftChildNode) + 1
            iterNode = node
            while iterNode.parentNode:
                if iterNode.parentNode.rightChildNode == iterNode:
                    rank += self._getTreeNodeCount(iterNode.parentNode.leftChildNode) + 1
                iterNode = iterNode.parentNode
            return rank - 1

    def getNodeByRank(self, rank: int) -> Union[TSBinaryNode, None]:
        if rank < 0:
            return None
        node = self.rootNode
        while node:
            leftCount = self._getTreeNodeCount(node.leftChildNode)
            if leftCount == rank:
                return node
            elif leftCount - 1 < rank:
                rank = rank - leftCount - 1
                node = node.rightChildNode
            else:
                node = node.leftChildNode
        return None

    def getMaxOrderNode(self) -> Union[TSBinaryNode, None]:
        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.rightChildNode:
                    iterNode = iterNode.rightChildNode
                else:
                    return iterNode

    def getMinOrderNode(self) -> Union[TSBinaryNode, None]:
        if not self.rootNode:
            return None
        else:
            iterNode = self.rootNode
            while iterNode:
                if iterNode.leftChildNode:
                    iterNode = iterNode.leftChildNode
                else:
                    return iterNode

    def deleteMaxOrderNode(self):
        node = self.getMaxOrderNode()
        if node:
            if node.parentNode:
                node.parentNode.rightChildNode = node.leftChildNode
            else:
                self.rootNode = node.leftChildNode
            if node.leftChildNode:
                node.leftChildNode.parentNode = node.parentNode
            node.leftChildNode = None
            node.parentNode = None

    def deleteMinOrderNode(self):
        node = self.getMinOrderNode()
        if node:
            if node.parentNode:
                node.parentNode.leftChildNode = node.rightChildNode
            else:
                self.rootNode = node.rightChildNode
            if node.rightChildNode:
                node.rightChildNode.parentNode = node.parentNode
            node.rightChildNode = None
            node.parentNode = None

    def beautifulPrint(self, onlyOrder: bool=False) -> Union[dict, None]:
        return self._beautifulPrint(self.rootNode, onlyOrder)

    def _beautifulPrint(self, node: Union[TSBinaryNode, None], onlyOrder: bool=False) -> Union[dict, list, None]:
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

    def balanced(self):
        orderedList = self.getOrderedList()
        if len(orderedList) > 2:
            self.rootNode = self._balanced(orderedList)

    def _balanced(self, orderedList: List[TSBinaryNode]) -> TSBinaryNode:
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
            leftNode = self._balanced(orderedList[:centerIndex])
            rightNode = self._balanced(orderedList[centerIndex + 1:])
            centerNode.parentNode = None
            centerNode.leftChildNode = leftNode
            centerNode.rightChildNode = rightNode
            leftNode.parentNode = centerNode
            rightNode.parentNode = centerNode
            return centerNode
