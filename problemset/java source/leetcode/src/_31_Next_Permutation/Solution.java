package _31_Next_Permutation;

class Solution {
    public void nextPermutation(int[] nums) {

        int n = nums.length;
        int i = n - 1;
        while (i >= 0) {
            for (int j = n - 1; j > i; --j) {
                if (nums[i] < nums[j]) {
                    int tmp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = tmp;
                    reverse(nums, i + 1, n - 1);
                    return;
                }
            }
            i--;
        }

        // can't find the next permutation, return lowest
        reverse(nums, 0, n - 1);
    }

    void reverse(int[] nums, int start, int end) {
        int i = start;
        int j = end;
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}