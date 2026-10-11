from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        postorder = [root.val]

        stack = deque([root.children])

        while len(stack) > 0:
            node = stack.pop()
            postorder.append(node.val)
            for child in node.children:
                stack.append(child)

        return postorder[::-1]