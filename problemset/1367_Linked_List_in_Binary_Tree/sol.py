from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubPath(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    if head is None:
        return True

    if root is None or root.val != head.val:
        return False

    return isSubPath(head.next, root.left) or isSubPath(head.next, root.right)


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        if root.val == head.val:
            if isSubPath(head, root):
                return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
