class Solution {
    public int[] searchRange(int[] nums, int target) {     
        
        int minx = find(nums, target);
        if (minx == -1 || nums[minx] != target) {
            return new int[]{-1, -1};
        }
        int maxx = find(nums, target + 1);
        if (maxx == -1) {
            maxx = nums.length;
        }
        return new int[] { minx, maxx - 1 };
    }

    // find minimal position element greater equal than targer
    private int find(int[] nums, int target) {
        int n = nums.length;
        int res = -1;
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = (l + r) >>> 1; // bitwise faster than div 2 :v 
            if (nums[mid] >= target) {
                res = mid;
                --r;
            } else {
                ++l;
            }
        }
        return res;
    }
}