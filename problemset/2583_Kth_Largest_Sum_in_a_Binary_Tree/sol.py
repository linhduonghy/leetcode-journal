# Definition for a binary tree node.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
            
        
        prev_level = 0
        cur_sum = 0
        sum_level = []
        
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if level > prev_level:
                sum_level.append(cur_sum)
                prev_level = level
                cur_sum = 0
            cur_sum += node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))            
            
        sum_level.append(cur_sum)
        
        if k > len(sum_level) - 1:
            return -1
        
        return sorted(sum_level[1:])[-k]
        
            