class Solution:
    def minSwaps(self, s: str) -> int:
        
        stack_size = 0
        for c in s:
            if c == '[':
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
        
        return (stack_size + 1) // 2