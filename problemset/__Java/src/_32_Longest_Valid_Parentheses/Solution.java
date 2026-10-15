package _32_Longest_Valid_Parentheses;

import java.util.Stack;

class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();

        int result = 0;
        int n = s.length();
        int[] F = new int[n];
        for (int i = 0; i < n; ++i) {
            if (s.charAt(i) == ')') {
                if (!stack.empty()) {
                    int l = stack.pop();
                    int num = i - l + 1;
                    if (l > 0) {
                        num += F[l - 1];
                    }
                    F[i] = num;
                    result = Math.max(result, num);
                }
            } else {
                stack.push(i);
            }
        }
        return result;
    }
}