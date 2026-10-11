import math

mod = int(1e9+7)
def exponent(n, k):
    res = 1
    while k > 0:
        if k % 2 == 1:
            res = (res * n) % mod
        n = (n * n) % mod
        k //= 2
    return res
    
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        n_even = math.ceil(n / 2)
        n_odd = n - n_even
        return (exponent(5, n_even) * exponent(4, n_odd)) % mod