class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # X = Q * Y + R
        # X = (2^a + .. + ) * Y + R
        # X = Y*2^a + Y*2^b + ... + R  ; Y*2^a = Y << a 
        # find a, b, ...

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            a = 0
            while dividend >= divisor << (a + 1): a += 1
            res += 1 << a
            dividend -= divisor << a
        res = res if sign else -res
        if res == 1<<31:
            return (1<<31)-1
        return res
    
if __name__ == "__main__":
    s = Solution()
    res = s.divide(-2147483648, 1)
    print (res)