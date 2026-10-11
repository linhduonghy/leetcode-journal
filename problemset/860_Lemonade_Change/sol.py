from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count5, count10 = 0, 0
        for bill in bills:
            print(bill, count5, count10)
            if bill == 5:
                count5 += 1
            elif bill == 10:
                if count5 == 0:
                    return False
                count10 += 1
                count5 -= 1
            else:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False
        return True
if __name__ == "__main__":
    
    s = Solution()
    print(s.lemonadeChange([5,5,5,10,5,20,5,10,5,20]))