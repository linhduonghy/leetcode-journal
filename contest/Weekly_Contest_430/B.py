
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        ans = ""
        for i in range(0, n):
            s = word[i]
            for j in range(i+1, n):
                if n - len(s) < numFriends:
                    break
                s += word[j]
            ans = max(ans, s)

        return ans
