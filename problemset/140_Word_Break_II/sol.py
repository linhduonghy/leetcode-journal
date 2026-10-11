from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        result = []
        def backtrack(s: str, wordDict: set, cur_index: int, current_sequence: List[str], result: List[str]):
            if cur_index == len(s):
                result.append(" ".join(current_sequence))
                return

            for index in range(cur_index + 1, len(s) + 1):
                word = s[cur_index:index]
                if word in wordDict:
                    current_sequence.append(word)
                    backtrack(s, wordDict, index, current_sequence, result)
                    current_sequence.pop()

        backtrack(s, wordDict, 0, [], result)
        return result