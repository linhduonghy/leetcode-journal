from typing import List
from collections import Counter
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        counter1 = Counter(message)
        counter2 = Counter(bannedWords)

        cnt = 0
        for k, v in counter1.items():
            if k in counter2:
                cnt += v
            if cnt >= 2:
                return True
        return False

if __name__ == '__main__':
    print(Solution().reportSpam(message=["uz","cm","ga","b","zm","p","jg","li","p"], bannedWords=["p","v","ki","o","n","b","ci","nv","k"]))