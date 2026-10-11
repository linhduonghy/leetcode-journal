
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        n = len(s)
        next_zero = [0] * n
        prev_zero = [0] * n
        count_prev_one = [0] * n
        count_next_one = [0] * (n + 1)
        cnt_zero = 0
        cnt_one = 0
        for i in range(n):
            if s[i] == '0':
                cnt_zero += 1
            else:
                cnt_one += 1
                prev_zero[i] = cnt_zero
                cnt_zero = 0
            count_prev_one[i] = cnt_one

        cnt_zero = 0
        cnt_one = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                cnt_zero += 1
            else:
                cnt_one += 1
                next_zero[i] = cnt_zero
                cnt_zero = 0
            count_next_one[i] = cnt_one

        res = 0
        for i in range(n):
            res = max(res, count_prev_one[i] + count_next_one[i + 1])
        i = 0
        while i < n:

            if s[i] == '1':
                j = i + 1
                while j < n and s[j] == '1': j += 1
                res = max(res, j - i)
                if next_zero[j - 1] > 0 and prev_zero[i] > 0:
                    # print(i, j - 1, prev_zero[i], next_zero[j - 1])
                    res = max(res, j - i + prev_zero[i] + next_zero[j - 1] + count_prev_one[i - prev_zero[i]] + count_next_one[j - 1 + next_zero[j - 1]])
                i = j
            else:
                i += 1
        return res

if __name__ == '__main__':
    Solution().maxActiveSectionsAfterTrade("1000100")
