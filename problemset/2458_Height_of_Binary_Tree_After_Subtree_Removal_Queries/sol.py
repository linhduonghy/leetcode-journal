# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_height = 0


    """
         Left and Right Traversal
         
         For any node, the height after removing its subtree simply the height of the tree 
         before reaching node. From left, and right 
         
    """

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        max_height_after_remove = [0] * 100001

        def traverse_left_right(root: Optional[TreeNode], current_height: int):
            if not root:
                return

            max_height_after_remove[root.val] = self.max_height
            self.max_height = max(self.max_height, current_height)
            traverse_left_right(root.left, current_height + 1)
            traverse_left_right(root.right, current_height + 1)

        def traverse_right_left(root: Optional[TreeNode], current_height: int):
            if not root:
                return
            max_height_after_remove[root.val] = max(max_height_after_remove[root.val], self.max_height)
            self.max_height = max(self.max_height, current_height)
            traverse_right_left(root.right, current_height + 1)
            traverse_right_left(root.left, current_height + 1)

        traverse_left_right(root, 0)
        self.max_height = 0
        traverse_right_left(root, 0)

        return [max_height_after_remove[v] for v in queries]
