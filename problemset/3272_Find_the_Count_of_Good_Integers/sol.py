from typing import List
import math
from itertools import permutations
from math import factorial
from collections import Counter

v1 = set()
ex = []
def valid_k_palindromic(digits: str, n: int, k: int, visited: set) -> int:
    temp = ''.join(sorted(list(digits)))
    if temp in visited:
        return 0
    visited.add(temp)
    unique_perms = set(permutations(digits))
    cnt = 0
    s1 = set()
    for p in unique_perms:
        p = ''.join(p)
        if p[0] == '0':
            continue
        num = 0
        if n % 2 == 0:
            num = int(p + p[::-1])
        else:
            num = int(p + p[:len(p) - 1][::-1])
        if num % k == 0:     
            tt = ''.join(sorted(list(str(num))))
            if tt not in s1:
                s1.add(tt)
                cnt += count_permutations(str(num))
                
    return cnt

def count_permutations(digits: str) -> int:
    def count_total(freq_map):
        total = sum(freq_map.values())
        denom = 1
        for count in freq_map.values():
            denom *= factorial(count)
        return factorial(total) // denom

    freq = Counter(digits)
    total_perms = count_total(freq)

    # If '0' is present, count how many permutations start with '0'
    if '0' in freq:
        freq['0'] -= 1
        if freq['0'] == 0:
            del freq['0']
        zero_leading_perms = count_total(freq)
    else:
        zero_leading_perms = 0

    valid = total_perms - zero_leading_perms
    return valid

class Solution:
    def __init__(self):
        self.ans = 0
        self.visited = set()
    def countGoodIntegers(self, n: int, k: int) -> int:
        def generate_palindrome(idx: int, n: int, half: int, current: List[str]):
            if idx == half:
                current_str = ''.join(current)
                self.ans += valid_k_palindromic(current_str, n, k, self.visited)
                return
            for digit in range(10):
                current.append(str(digit))
                generate_palindrome(idx + 1, n, half, current)
                current.pop()
        
        generate_palindrome(0, n, math.ceil(n / 2), [])
        return self.ans
    
if __name__ == '__main__':
    Solution().countGoodIntegers(5, 6)