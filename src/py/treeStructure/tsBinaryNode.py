import time
import uuid
from typing import Union


class TSBinaryNode:

    def __init__(self, order: float = time.time(), value=None):
        self.id: str = str(uuid.uuid4())
        self.order: float = order
        self.value = value
        self.leftChildNode: Union[TSBinaryNode, None] = None
        self.rightChildNode: Union[TSBinaryNode, None] = None
        self.parentNode: Union[TSBinaryNode, None] = None
