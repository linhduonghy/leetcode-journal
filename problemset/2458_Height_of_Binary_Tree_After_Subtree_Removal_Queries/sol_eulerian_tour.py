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
        In the preorder traversal of a tree, a subtree is traversed in consecutive order 
        We can flatten the traversal order of a tree to the 1d array 
        then find the max depth left and right subtree in array
        
        We can use Eulerian tour to flatten the traversal order in 1d array 
    """
    
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        pass