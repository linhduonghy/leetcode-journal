from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        n = len(s)
        last_pos = [0] * 26
        for c in range(0, 26):
            last_pos[c] = s.rfind(chr(c + 97))
        cur_max = 0
        left = 0
        for i in range(n):
            last_id = last_pos[ord(s[i]) - 97]
            if last_id > cur_max:
                cur_max = last_id
            elif i == cur_max:
                result.append(i - left + 1)
                left = i + 1
                cur_max = i + 1
                
        return result