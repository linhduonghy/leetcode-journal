from typing import Optional
import re

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
import re

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        trav = re.findall("\\d+|-+", traversal)
        root = TreeNode(int(trav[0]))
        depth_map = dict()
        def dfs(root: TreeNode, cur_depth: int, index):
            if index >= len(trav):
                return
            depth_map[cur_depth] = root
            d = len(trav[index])
            if d == cur_depth + 1:
                newNode = TreeNode(int(trav[index + 1]))
                if not root.left:
                    root.left = newNode
                else:
                    root.right = newNode
                dfs(newNode, d, index + 2)
            else: 
                dfs(depth_map[d - 1], d - 1, index)
            
        dfs(root, 0, 1)
        return root
        