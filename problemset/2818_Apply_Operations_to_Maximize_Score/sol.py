from typing import List
from collections import deque

def get_primes(limit: int) -> List[int]:
    is_prime = [True] * (limit + 1)
    primes = []

    for num in range(2, limit + 1):
        if not is_prime[num]:
            continue
        primes.append(num)
        for v in range(num * num, limit + 1, num):
            is_prime[v] = False

    return primes
    
mod = int(1e9 + 7)
def power(base, exponent):
    res = 1
    while exponent > 0:
        if exponent % 2:
            res = (res * base) % mod
        base = (base * base) % mod
        exponent //= 2

    return res
    
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        limit = max(nums)
        primes = get_primes(limit)   
        c_primes = [0] * n
        for i in range(n):
            v = nums[i]
            for prime in primes:
                if prime * prime > v:
                    break
                if v % prime == 0:
                    c_primes[i] += 1
                    while v % prime == 0:
                        v //= prime
            if v >= 2:
                c_primes[i] += 1
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        stack = deque()
        for i in range(n):
            while stack and c_primes[stack[-1]] < c_primes[i]:
                top_idx = stack.pop()
                next_dominant[top_idx] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)
        num_of_subarrays = [(i - prev_dominant[i]) * (next_dominant[i] - i) for i in range(n)]
        score = 1
        sorted_eles = sorted([(num, i) for i, num in enumerate(nums)], reverse=True, key= lambda x : x[0])
        cur_index = 0
        while k > 0:
            num, index = sorted_eles[cur_index]
            operations = min(k, num_of_subarrays[index])
            score = (score * power(num, operations)) % mod
            k -= operations        
            cur_index += 1    
        
        return score