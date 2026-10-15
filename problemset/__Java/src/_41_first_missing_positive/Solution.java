package _41_first_missing_positive;

class Solution {
    public int firstMissingPositive(int[] nums) {

        int n = nums.length;

        for (int i = 0; i < n; ++i) {
            if (nums[i] > n || nums[i] <= 0) {
                nums[i] = n + 1;
            }
        }

        for (int i = 0; i < n; ++i) {
            int num = Math.abs(nums[i]);
            if (num > n) {
                continue;
            }

            num -= 1;
            if (nums[num] > 0) {
                nums[num] = -nums[num];
            }
        }

        for (int i = 0; i < n; ++i) {
            if (nums[i] >= 0) {
                return i + 1;
            }
        }

        return n + 1;

    }
}