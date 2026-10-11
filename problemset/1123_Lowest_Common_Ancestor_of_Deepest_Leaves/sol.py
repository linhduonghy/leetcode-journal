# Definition for a binary tree node.

from typing import Optional
from typing import Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root: TreeNode) -> Tuple[int, TreeNode]:
            if not root:
                return 0, root
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            elif l[0] < r[0]:
                return r[0] + 1, r[1]
            return l[0] + 1, root
        
        return dfs(root)[1]
            