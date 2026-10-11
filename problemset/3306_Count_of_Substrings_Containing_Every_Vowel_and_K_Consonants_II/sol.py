
def atLeastVowel(counter: list):
    return (counter[0] >= 1 and counter[4] >= 1 and counter[8] >= 1
            and counter[14] >= 1 and counter[20] >= 1)

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        counter = [0] * 26
        next_consonants = [0] * n
        next_consonants_index = n
        for i in range(n - 1,  -1, -1):
            next_consonants[i] = next_consonants_index
            if word[i] not in vowels:
                next_consonants_index = i
        ans = 0
        l, r = 0, 0
        consonants = 0
        while r < n:
            counter[ord(word[r]) - ord('a')] += 1
            if word[r] not in vowels:
                consonants += 1
            while l < n and atLeastVowel(counter) and consonants >= k:
                if consonants == k:
                    ans += next_consonants[r] - r
                counter[ord(word[l]) - ord('a')] -= 1
                if word[l] not in vowels:
                    consonants -= 1
                l += 1
            r += 1
        return ans