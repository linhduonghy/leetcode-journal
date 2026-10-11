
//* Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}


function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {

    // reverse list node
    let reverseListNode = reverse(head);
    if (n == 1) {
        return reverse(reverseListNode.next);
    }
    let result = reverseListNode;
    --n;
    let prevNode: ListNode;
    while (n > 0) {
        prevNode = reverseListNode;
        reverseListNode = reverseListNode.next;
        --n;
    }

    prevNode.next = reverseListNode.next;

    return reverse(result);
};

// reverse Listnode 
function reverse(head: ListNode): ListNode {
    if (head == null) {
        return null;
    }
    let current = head.next;
    head.next = null;
    let reverseListNode = head;
    while (current != null) {
        let curTemp = current.next;
        current.next = reverseListNode;
        reverseListNode = current;
        current = curTemp;
    }
    return reverseListNode;
}