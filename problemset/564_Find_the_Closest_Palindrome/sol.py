class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        N = int(n)
        
        length = len(n)
        leftHalf = int(n[:(length + 1)//2])
        
        def generatePalindromeFromLeft(leftHalf: int, isEven: int) -> int:
            left = str(leftHalf)
            return int(left + left[::-1] if isEven else left + left[-2::-1])
        
        candidates = [generatePalindromeFromLeft(leftHalf, length % 2 == 0), 
                      generatePalindromeFromLeft(leftHalf - 1, length % 2 == 0),
                      generatePalindromeFromLeft(leftHalf + 1, length % 2 ==0),
                      10**(length - 1) - 1,
                      10**(length) + 1]
        
        differentWithN = [(abs(N - c), c) for c in candidates]
        differentWithN.sort(key = lambda e : (e[0], e[1]))
        
        return str(differentWithN[0][1]) if differentWithN[0][1] != N else str(differentWithN[1][1])
    
if __name__ == "__main__":
    print(Solution().nearestPalindromic("129329980012120"))