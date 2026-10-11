
'''
    a xor a = 0
    b xor 0 = b
    => a xor b xor a = b
    
    prefixXor[i] = a[0] xor a[1] xor .... xor a[i]
    
    => xor(a[i..j]) = prefixXor[j] xor prefixXor[i - 1]
    
'''

from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        preXor = [0 for i in range(len(arr))]
        preXor[0] = arr[0]
        for i in range(1, len(arr)):
            preXor[i] = preXor[i - 1] ^ arr[i]
        
        res = [0 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            
            if query[0] == 0:
                res[i] = preXor[query[1]]
            else:
                res[i] = preXor[query[1]] ^ preXor[query[0] - 1]
        return res