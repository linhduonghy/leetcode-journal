class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        if sentence1 == sentence2:
            return True

        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        n = len(s1)
        m = len(s2)

        if n == m:
            return False

        prefixLen = 0
        suffixLen = 0
        while prefixLen < n and prefixLen < m and s1[prefixLen] == s2[prefixLen]: prefixLen += 1
        while n - suffixLen - 1 >= 0 and m - suffixLen - 1 >= 0 and s1[n - suffixLen - 1] == s2[m - suffixLen - 1]: suffixLen += 1

        print(prefixLen, suffixLen)
        if n < m:
            if prefixLen == n or suffixLen == n:
                return True
            if prefixLen + suffixLen < n:
                return False

        if m < n:
            if prefixLen == m or suffixLen == m:
                return True
            if prefixLen + suffixLen < m:
                return False

        return True



