class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res = 0
        for p in range(2, n >> 1):
            if n > p: break
            count = 0
            while n % p == 0: 
                count += 1 
                n = n // p
            res += p * count
        if n > 1:
            res += n
        return res

if __name__ == "__main__":
    print(Solution().minSteps(1000))