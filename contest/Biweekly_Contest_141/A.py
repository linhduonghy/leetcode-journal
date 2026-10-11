from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)

        for i in range(len(nums)):
            x = nums[i]
            if x == 2:
                continue
            bit_cnt = x.bit_length()
            s = ('{0:' + str(bit_cnt) + 'b}').format(x)
            n = len(s) - 1
            while n >= 0 and s[n] == '1': n -= 1
            if n >= 0:
                n = n + 1
                print(s, n + 1, end=',')
                s = s[:n] + '0'
                for _ in range(n + 1, bit_cnt):
                    s += '1'
                print(s)
                ans[i] = int(s, 2)
            else:
                ans[i] = pow(2, bit_cnt - 1) - 1

        return ans