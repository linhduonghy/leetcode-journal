def invert(s: str):
    return ''.join('0' if c == '1' else '1' for c in s)

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        cur = "0"
        for _ in range(0, n):
            cur = cur + "1" + invert(cur)[::-1]
        
        return cur[k - 1]