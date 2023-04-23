from .tsBinaryNode import TSBinaryNode
from typing import Union
from .tsConstants import TSConstants


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
                        if iterNode.parentNode.leftChildNode == iterNode:
                            iterNode.parentNode.leftChildNode = None
                        else:
                            iterNode.parentNode.rightChildNode = None
                    elif iterNode.leftChildNode and not iterNode.rightChildNode:
                        if iterNode.parentNode.leftChildNode == iterNode:
                            iterNode.parentNode.leftChildNode = iterNode.leftChildNode
                        else:
                            iterNode.parentNode.rightChildNode = iterNode.leftChildNode
                        iterNode.leftChildNode.parentNode = iterNode.parentNode
                    elif not iterNode.leftChildNode and iterNode.rightChildNode:
                        if iterNode.parentNode.leftChildNode == iterNode:
                            iterNode.parentNode.leftChildNode = iterNode.rightChildNode
                        else:
                            iterNode.parentNode.rightChildNode = iterNode.rightChildNode
                        iterNode.rightChildNode.parentNode = iterNode.parentNode
                    else:
                        maxNodeInLeft = iterNode.leftChildNode
                        if not maxNodeInLeft.rightChildNode:
                            if iterNode.parentNode.leftChildNode == iterNode:
                                iterNode.parentNode.leftChildNode = maxNodeInLeft
                            else:
                                iterNode.parentNode.rightChildNode = maxNodeInLeft
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

                            if iterNode.parentNode.leftChildNode == iterNode:
                                iterNode.parentNode.leftChildNode = maxNodeInLeft
                            else:
                                iterNode.parentNode.rightChildNode = maxNodeInLeft
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

    def searchNode(self, order: float) -> Union[TSBinaryNode, None]:
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
        if not self.rootNode:
            return -1
        return self._getTreeHeight(self.rootNode)

    def _getTreeHeight(self, node: Union[TSBinaryNode, None]) -> int:
        if not node:
            return 0
        leftHeight = self._getTreeHeight(node.leftChildNode)
        rightHeight = self._getTreeHeight(node.rightChildNode)
        return max(leftHeight, rightHeight) + 1

    def getTreeNodeCount(self) -> int:
        return self._getTreeNodeCount(self.rootNode)

    def _getTreeNodeCount(self, node: Union[TSBinaryNode, None]) -> int:
        if not node:
            return 0
        leftNodeCount = self._getTreeNodeCount(node.leftChildNode)
        rightNodeCount = self._getTreeNodeCount(node.rightChildNode)
        return leftNodeCount + 1 + rightNodeCount

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
        self.deleteNodeByOrder(node.order)

    def deleteMinOrderNode(self):
        node = self.getMinOrderNode()
        self.deleteNodeByOrder(node.order)

    def beautifulPrint(self) -> Union[dict, None]:
        return self._beautifulPrint(self.rootNode)

    def _beautifulPrint(self, node: Union[TSBinaryNode, None]) -> Union[dict, None]:
        if not node:
            return None
        else:
            return {
                TSConstants.BinaryNode.order: node.order,
                TSConstants.BinaryNode.value: node.value,
                TSConstants.BinaryNode.leftChildNode: self._beautifulPrint(node.leftChildNode),
                TSConstants.BinaryNode.rightChildNode: self._beautifulPrint(node.rightChildNode)
            }
