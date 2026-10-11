from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if root is None:
            return []

        postorder = []

        def dfs(node: Node, postorder: List[int]):
            if node is None:
                return

            if node.children is None:
                postorder.append(node.val)

            for x in node.children:
                dfs(x, postorder)

        return postorder

