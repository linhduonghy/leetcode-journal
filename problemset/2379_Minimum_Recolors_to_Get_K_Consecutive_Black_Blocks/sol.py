class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        n = len(blocks)
        min_ops = n
        for i in range(n):
            if i >= k and blocks[i - k] == 'W' and white_count > 0:
                white_count -= 1
            if blocks[i] == 'W':
                white_count += 1
            if i >= k - 1:
                min_ops = min(min_ops, white_count)

        return min_ops



