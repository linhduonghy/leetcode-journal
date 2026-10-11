# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        sum = {}
        def findSum(root: Optional[TreeNode], level: int):
            
            if not root:
                return
            
            if level not in sum:
                sum[level] = 0
            
            sum[level] += root.val
            
            findSum(root.left, level + 1)
            findSum(root.right, level + 1)

        findSum(root, 0)
        
        
        def dfs(root: Optional[TreeNode], level: int):
            if level == 0:
                root.val = 0
            childSum = 0
            if root.left:
                childSum += root.left.val
            if root.right:
                childSum += root.right.val
            
            if root.left:
                root.left.val = sum[level + 1] - childSum
                dfs(root.left, level + 1)
            if root.right:
                root.right.val = sum[level + 1] - childSum
                dfs(root.right, level + 1)
                
            
        dfs(root, 0)
        
        return root
        
        