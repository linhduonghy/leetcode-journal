/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function middleNode(head: ListNode | null): ListNode | null {
    //     let count = 0;

    //     let currentNode = head;

    //     while (currentNode != null) {
    //         currentNode = currentNode.next;
    //         ++count;
    //     }


    //     if ((count & 1) == 0) {
    //         count = (count / 2) + 1;
    //     } else {
    //         count = (count + 1) / 2;
    //     }

    //     while (count > 1) {
    //         head = head.next;
    //         --count;
    //     }

    // fast and slow pointer :v

    let fast = head, slow = head;

    while (fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
    }
    return slow;
};