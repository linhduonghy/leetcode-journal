import java.util.Stack;

class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> st = new Stack<>();        
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '#') {
                if (!st.isEmpty()) {
                    st.pop();
                }
            } else {
                st.push(s.charAt(i));
            }
        }
        
        Stack<Character> st2 = new Stack<>();
        for (int i = 0; i < t.length(); ++i) {
            if (t.charAt(i) == '#') {
                if (!st2.isEmpty()) {
                    st2.pop();
                }
            } else {
                st2.push(t.charAt(i));
            }
        }
        return st.toArray().equals(st2.toArray());
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.backspaceCompare("a#c", "b"));
    }
}