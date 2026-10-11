class Solution:
    def maximumLength(self, s: str) -> int:
        
        freq = {}
        
        for i in range(len(s)):
            j = i
            sub = ""        
            while j < len(s) and s[j] == s[i]:
                sub += s[j]
                if sub not in freq:
                    freq[sub] = 0
                freq[sub] += 1
                j += 1 
        ans = -1
        for k, v in freq.items():
            if v >= 3:
                print(k, v)
                ans = max(ans, len(k))
        return ans