class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 3:
            return (int(s[0]) + int(s[1])) % 10 == (int(s[1]) + int(s[2])) % 10
        g = len(s) - 2
        l = 0
        r = len(s) - 2
        sum1 = (int(s[l]) + int(s[r]))
        l += 1
        r -= 1
        while l <= r:
            if l == r:
                sum1 += (int(s[l]) * g)
            else:
                sum1 += (int(s[l]) * g + int(s[r]) * g)
            l += 1
            r -= 1
            g += 2
        print(sum1)
        g = len(s) - 2
        l = 1
        r = len(s) - 1
        sum2 = (int(s[l]) + int(s[r]))
        l += 1
        r -= 1

        while l <= r:
            if l == r:
                sum2 += (int(s[l]) * g)
            else:
                sum2 += (int(s[l]) * g + int(s[r]) * g)
            l += 1
            r -= 1
            g += 2
        print(sum2)
        return sum1 == sum2

if __name__ == '__main__':
    s = Solution()
    s.hasSameDigits("8506969")