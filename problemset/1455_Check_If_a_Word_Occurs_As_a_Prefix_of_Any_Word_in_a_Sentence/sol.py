class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sen_arr = sentence.split(" ")
        for i, sen in enumerate(sen_arr):
            if sen.startswith(searchWord):
                return i + 1
        
        return -1
            