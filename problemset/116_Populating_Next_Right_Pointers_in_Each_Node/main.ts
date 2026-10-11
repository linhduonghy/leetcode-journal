
//  Definition for Node.
class Node1 {
    val: number
    left: Node1 | null
    right: Node1 | null
    next: Node1 | null
    constructor(val?: number, left?: Node1, right?: Node1, next?: Node1) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
        this.next = (next === undefined ? null : next)
    }
}


function connect(root: Node1 ): Node1 | null {

    if (!root) {
        return root;
    }

    next(root.left, root.right);
    return root;

};

function next(rootL: Node1, rootR: Node1) {


    if (!rootL) {
        return;
    }

    rootL.next = rootR;

    // node left: node.left.next = node.right;
    next(rootL.left, rootL.right);

    // node right: node.left.next = node.right;
    next(rootR.left, rootR.right);

    // child right (node left) -> child left (node right)
    next(rootL.right, rootR.left);

}