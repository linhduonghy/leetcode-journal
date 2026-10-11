from typing import List
import math
import heapq

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
        c_primes = [0] * n
        for i in range(n):
            v = nums[i]
            for prime in range(2, math.floor(math.sqrt(v)) + 1):
                if v % prime == 0:
                    c_primes[i] += 1
                    while v % prime == 0: v //= prime
            if v >= 2:
                c_primes[i] += 1
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        stack = []
        for i in range(n):
            while stack and c_primes[stack[-1]] < c_primes[i]:
                top_idx = stack.pop()
                next_dominant[top_idx] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)
        pq = [(-nums[i], i) for i in range(n)]
        heapq.heapify(pq)
        num_of_subarrays = [(i - prev_dominant[i]) * (next_dominant[i] - i) for i in range(n)]
        score = 1
        while k > 0:
            num, index = heapq.heappop(pq)
            num = -num
            operations = min(k, num_of_subarrays[index])
            score = (score * power(num, operations)) % mod
            k -= operations            
        
        return score