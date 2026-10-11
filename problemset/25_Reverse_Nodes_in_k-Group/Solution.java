//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    void printList() {
        while (headA != null) {
            System.out.println(head.val + " ");
            head = head.next;
        }
    }
}

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        return null;

    }

    public static void main(String[] args) {
        ListNode listNode = new ListNode();
        ListNode head = listNode;
        for (int i = 1; i <= 5; ++i) {
            listNode.val = i;
            listNode.next = new ListNode();
            listNode = listNode.next;
        }

        Solution s = new Solution();
        s.reverseKGroup(head, 2);
    }
}