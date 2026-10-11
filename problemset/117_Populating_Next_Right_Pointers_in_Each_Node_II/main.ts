/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     left: Node | null
 *     right: Node | null
 *     next: Node | null
 *     constructor(val?: number, left?: Node, right?: Node, next?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function connect(root: Node | null): Node | null {
    
    if (!root) {
        return root;
    }
    root.next = null;
    if (root.right) {
       next(root.right, root, false);
    }     
    if (root.left) {
        next(root.left, root, true);
    }
    
    return root;
};

function next(root: Node, parent: Node, left: boolean) {
    if (left) {
        if (parent.right) {
            root.next = parent.right;    
        } else {
            let temp = parent.next;
            while (temp && getLeftNode(temp) == null) {
                temp = temp.next;
            }
            root.next = getLeftNode(temp);
        }
    } else {
        let temp = parent.next;
        while (temp && getLeftNode(temp) == null) {
            temp = temp.next;
        }
        root.next = getLeftNode(temp);       
    }
    
    if (root.right) {
       next(root.right, root, false);
    }     
    
    if (root.left) {
        next(root.left, root, true);
    }
    
}

function getLeftNode(node: Node) {
    if (node == null) {
        return null;
    }
    if (node.left) {
        return node.left;
    }
    if (node.right) {
        return node.right;
    }
}