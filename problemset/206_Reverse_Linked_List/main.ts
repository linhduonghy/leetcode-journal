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

 function reverseList(head: ListNode | null): ListNode | null {    
    
    if (!head) {
        return head;
    }
    
    let revertHead = head;
    head = head.next;    
    revertHead.next = null;    
    while (head) {        
        let temp = head.next;        
        head.next = revertHead;        
        revertHead = head;
        head = temp;
    }
    
    return revertHead;
};