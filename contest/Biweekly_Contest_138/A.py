class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:

        s1 = str(num1)
        s2 = str(num2)
        s3 = str(num3)

        while len(s1) < 4: s1 = '0' + s1
        while len(s2) < 4: s2 = '0' + s2
        while len(s3) < 4: s3 = '0' + s3

        result = ''

        for i in range(4):
            result = result + min(s1[i], s2[i], s3[i])

        return int(result)

        
if __name__ == "__main__":
    
    s = Solution()
    s.generateKey( 987, 879, 798)