# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
def dfs(left_child: Optional[TreeNode], right_child: Optional[TreeNode], level: int):
    if left_child is None or right_child is None:
        return

    if level % 2 == 0:
        temp = left_child.val
        left_child.val = right_child.val
        right_child.val = temp

    dfs(left_child.left, right_child.right, level + 1)
    dfs(left_child.right, right_child.left, level + 1)

class Solution:

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs(root.left, root.right, 1)
        return root


