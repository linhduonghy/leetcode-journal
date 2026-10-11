class Solution:
    def minLength(self, s: str) -> int:

        stack = []
        del_list = ["AB", "CD"]
        stack.append(s[0])
        for i in range(1, len(s)):
            if len(stack) > 0 and (stack[-1] + s[i]) in del_list:
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)