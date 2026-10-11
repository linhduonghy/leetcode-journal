/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

 function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    
    return dfs(root, subRoot);
    
};

function dfs(root: TreeNode, subRoot: TreeNode) {
    if (root == null) {
        return false;
    }
    if (isIdentical(root, subRoot)) {
        return true;
    }
    return dfs(root.left, subRoot) || dfs(root.right, subRoot);
}

function isIdentical(node1: TreeNode, node2: TreeNode) {
    if (node1 == null && node2 == null) {
        return true;
    }
    
    if (node1 && node2 && node1.val == node2.val) {
        return isIdentical(node1.left, node2.left) && isIdentical(node1.right, node2.right);
    } else {
        return false;
    }
}