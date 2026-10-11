from typing import List
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:

        n = len(energyDrinkA)
        dpA = [0 for _ in range(n)]
        dpB = [0 for _ in range(n)]
        
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        
        for i in range(1, n):
            
            dpA[i] = max(dpA[i - 1] + energyDrinkA[i], dpB[i - 1])
            dpB[i] = max(dpB[i - 1] + energyDrinkB[i], dpA[i - 1])
        
        return max(dpA[-1], dpB[-1])
        
if __name__ == "__main__":
    
    s = Solution()
    print(s.maxEnergyBoost([5,5,6,3,4,3,3,4], [5,3,3,4,4,6,6,3]))
    