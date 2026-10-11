from typing import List

limit = 1000000
greatest_divisors = [0] * (limit + 1)
for i in range(2, limit // 2 + 1):
    # For each i, update its multiples with i as their greatest divisor
    for j in range(2 * i, limit + 1, i):
        greatest_divisors[j] = i
def query_greatest_proper_divisor(n):
    if n <= 1:
        return None  # No proper divisor for n <= 1
    return greatest_divisors[n]

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        cnt = 0
        cur = n - 2
        next_value = nums[-1]
        while cur >= 0:
            while nums[cur] > next_value:
                greatest_proper_divisor = query_greatest_proper_divisor(nums[cur])
                if not greatest_proper_divisor:
                    return -1
                nums[cur] = nums[cur] // greatest_proper_divisor
                cnt += 1
            next_value = nums[cur]
            cur -= 1
        return cnt

if __name__ == '__main__':
    print(Solution().minOperations(
        [149, 659, 2389, 7499, 21419, 24043, 26489, 62687, 69193, 71353, 110581, 118621, 126337, 144577, 146837, 147827,
         151643, 152039, 169007, 183283, 188827, 192971, 207629, 222059, 241537, 251177, 280751, 282461, 305873, 339799,
         354313, 357977, 366881, 380621, 383041, 421493, 427993, 444001, 450803, 460063, 461051, 469849, 475421, 482051,
         486329, 491159, 507589, 518743, 520759, 522959, 535159, 547399, 562997, 597521, 613969, 614503, 622247, 632987,
         654089, 685513, 689831, 696349, 699793, 708667, 711967, 715229, 723721, 728267, 733301, 736279, 742199, 753691,
         769207, 776179, 778111, 785413, 794111, 798823, 806821, 820541, 820991, 822589, 833893, 836789, 852613, 857551,
         868103, 891679, 893161, 894247, 919417, 929063, 939823, 945677, 963659, 969481, 973957, 982843, 983113,
         998681]))
