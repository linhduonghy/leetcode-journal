class Solution:
    def compressedString(self, word: str) -> str:

        c = 1
        result = ''
        for i in range(1, len(word)):
            if word[i] != word[i-1] and c != 0:
                result += str(c) + word[i - 1]
                c = 1
            else:
                c += 1
                if c == 9:
                    c = 0
                    result += '9' + word[i]
        if c > 0:
            result += str(c) + word[-1]
        return result