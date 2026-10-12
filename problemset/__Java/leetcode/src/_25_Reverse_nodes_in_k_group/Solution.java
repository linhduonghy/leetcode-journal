package _25_Reverse_nodes_in_k_group;

import java.util.List;

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

    void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }
}

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {

        ListNode result = new ListNode(-1);
        ListNode _result = result;
        ListNode kNodes = new ListNode(-1);
        ListNode headTmp = kNodes;
        int counter = 0;
        while (head != null) {

            kNodes.val = head.val;

            counter += 1;
            head = head.next;

            if (counter < k && head != null) {
                kNodes.next = new ListNode(-1);
                kNodes = kNodes.next;
            }
            if (counter == k) {
                result.next = reverseNode(headTmp);
                while (result.next != null) {
                    result = result.next;
                }
                kNodes = new ListNode(-1);
                headTmp = kNodes;
                counter = 0;

            }
        }

        if (k > 1 && headTmp.val > -1) {
            result.next = headTmp;
        }
        return _result.next;
    }

    static ListNode reverseNode(ListNode node) {
        ListNode prev = node;
        ListNode cur = node.next;
        prev.next = null;
        while (cur != null) {
            ListNode tmp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = tmp;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode listNode = new ListNode(1);
        ListNode head = listNode;
        for (int i = 2; i <= 2; ++i) {
            listNode.next = new ListNode(i);
            listNode = listNode.next;
        }
        Solution s = new Solution();
        head.printList(s.reverseKGroup(head, 2));
    }
}