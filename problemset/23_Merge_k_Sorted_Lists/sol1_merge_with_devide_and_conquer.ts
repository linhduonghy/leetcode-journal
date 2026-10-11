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

 function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    
    if (lists.length == 0) {
        return null;
    }
    return mergeListsDQ(lists, 0, lists.length - 1);
    
};


function mergeListsDQ(lists: Array<ListNode>, l: number, r: number): ListNode {
    if (l == r) {
        return lists[l];
    }
    
    let mid = (l + r) >> 1;
    
    let leftListNode = mergeListsDQ(lists, l, mid);
    let rightListNode = mergeListsDQ(lists, mid + 1, r);
    
    return mergeTwoList(leftListNode, rightListNode);
}

function mergeTwoList(list1: ListNode, list2: ListNode): ListNode {
    if (list1 == null) {
        return list2;
    }
    if (list2 == null) {
        return list1;
    }
    
    if (list1.val < list2.val) {
        list1.next = mergeTwoList(list1.next, list2);
        return list1;
    } else {
        list2.next = mergeTwoList(list1, list2.next);
        return list2;
    }
}