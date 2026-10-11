package leetcode._16_3Sum_Closest;

import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        Arrays.sort(nums);
        int n = nums.length;
        int res = -1;
        int minn = 30000;
        for (int i = 0; i < n - 2; ++i) {                        
            int l = i + 1, r = n - 1;
            while (l < r) {
                
                int sum = nums[i] + nums[l] + nums[r];
                
                if (sum == target) {
                    return target;
                }
                
                if (Math.abs(sum - target) < minn) {
                    minn = Math.abs(sum - target);
                    res = sum;
                }
                if (sum > target ) {
                    --r;
                } else {
                    ++l;
                }
            }
        }
        
        return res;
    }
}