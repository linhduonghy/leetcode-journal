from typing import List, Dict

class Node:
        
    def __init__(self, next: dict, count):
        self.next = next
        self.count = count
    
class Trie:
    def __init__(self):
        self.root = Node({}, 0)
        
    def insert(self, word: str):
        cur = self.root 
        for c in word:
            c1 = ord(c) - ord('a')
            if c1 not in cur.next:
                node = Node({}, 1)
                cur.next[c1] = node
            else:
                node = cur.next[c1]
                node.count += 1
            cur = cur.next[c1]            
    
    def traverse(self, word: str) -> int:
        cnt = 0
        cur = self.root
        for c in word:
            c1 = ord(c) - ord('a')
            cnt += cur.next[c1].count 
            cur = cur.next[c1]
        return cnt
            
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)                
        
        res = []
        for word in words:
            res.append(trie.traverse(word))
        
        return res
        
        
            