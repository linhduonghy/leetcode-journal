class Solution:
    def smallestNumber(self, n: int) -> int:
        
        len = n.bit_length()

        return int("".join(['1' for _ in range(len)]), 2)

if __name__ == '__main__':
    print(Solution().smallestNumber(10))