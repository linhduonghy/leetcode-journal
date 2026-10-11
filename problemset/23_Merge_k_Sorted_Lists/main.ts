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

    let mergeList: ListNode = new ListNode();
    
    let result = mergeList;
    
    while (true) {
        
        let indexMinOfLists = find(lists);
        
        if (indexMinOfLists == null) {
            break;
        }
        
        mergeList.next = new ListNode(lists[indexMinOfLists].val);
        mergeList = mergeList.next;
        lists[indexMinOfLists] = lists[indexMinOfLists].next;
    }
    
    return result.next;
};

function find(lists: Array<ListNode>): number {
    
    let minId: number = null;
    let minValue = 10001; // 1e4+1
        
    for (let i = 0; i < lists.length; ++i) {
        if (lists[i] && minValue > lists[i].val) {
            minValue = lists[i].val;
            minId = i;
        }
    }
    
    return minId;
}