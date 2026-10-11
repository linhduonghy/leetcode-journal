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

 function deleteDuplicates(head: ListNode | null): ListNode | null {
    
    let flag = false;
    while (head && head.next) {
        if (head.val == head.next.val) {
            head = head.next;
            flag = true;
        } else if (flag) {
            head = head.next;
            flag = false;
        } else {
            break;
        }
    }
    
    if (flag) {
        head = head.next;
    }
    
    let current = head;
    let prev = current;
    flag = false;
    while (current && current.next) {
        if (current.val == current.next.val) {
            current.next = current.next.next;
            flag = true;
        } else if (flag) {
            prev.next = current.next;
            current = prev.next;
            flag = false;
        } else {
            prev = current;
            current = current.next;
            flag = false;
        }
    }
    if (flag) {
        prev.next = current.next;
    }
    return head;
};