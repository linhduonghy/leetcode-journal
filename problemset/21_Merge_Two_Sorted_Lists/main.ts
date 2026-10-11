
//   Definition for singly-linked list.
// class ListNode {
//     val: number
//     next: ListNode | null
//     constructor(val?: number, next?: ListNode | null) {
//         this.val = (val === undefined ? 0 : val)
//         this.next = (next === undefined ? null : next)
//     }
// }


function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {

    let result: ListNode = new ListNode();
    let current = result;
    while (l1 != null && l2 != null) {
        if (l1.val < l2.val) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }
    if (l1 == null) {
        current.next = l2;
    } else {
        current.next = l1;
    }
    return result.next;
};