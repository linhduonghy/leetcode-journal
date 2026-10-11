package _27_Remove_Element;

public class Solution {

    public int removeElement(int[] nums, int val) {

        int l = 0, r = nums.length - 1;
        int t = -1;
        while (l < r) {
            while (l < r && nums[l] != val) {
                l++;
            }
            while (l < r && nums[r] == val) {
                r--;
            }
            t = nums[l];
            nums[l] = nums[r];
            nums[r] = t;

        }

        l = 0;
        while (l < nums.length && nums[l] != val) {
            l += 1;
        }
        return l;
    }

}