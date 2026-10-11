from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)

        freq = []
        for c in sorted(counter.keys(), reverse=True):
                freq.append([c, counter[c]])
        i, n = 0, len(freq)
        ans = []
        count = 0
        while i < n:
            if freq[i][1] > 0:
                if count < repeatLimit:
                    ans.append(freq[i][0])
                    freq[i][1] -= 1
                    count += 1
                else:
                    j = i + 1
                    while j < n:
                        if freq[j][1] > 0:
                            ans.append(freq[j][0])
                            freq[j][1] -= 1
                            count = 0
                            break
                        j += 1
                    if j == n:
                        break
            else:
                count = 0
                i += 1
        return ''.join(ans)

if __name__ == '__main__':
    print(Solution().repeatLimitedString("aababab", 2))