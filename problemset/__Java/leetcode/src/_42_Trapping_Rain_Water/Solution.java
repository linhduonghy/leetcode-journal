package leetcode._42_Trapping_Rain_Water;

class Solution {
    public int trap(int[] height) {

        int n = height.length;

        int[] fl = new int[n];

        fl[0] = 0;
        for (int i = 1; i < n; ++i) {
            if (height[i] > height[fl[i - 1]]) {
                fl[i] = i;
            } else {
                fl[i] = fl[i - 1];
            }
        }

        int[] maxR = new int[n];
        maxR[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            maxR[i] = Math.max(maxR[i + 1], height[i]);
        }

        int imax = n - 1;
        while (imax >= 1 && height[imax] <= height[imax - 1]) imax -= 1;
        int res = 0;
        for (int i = n - 2; i >= 0; --i) {
            if (fl[i] == i) {
                res += calWater(height, maxR, i, imax);
                imax = i;
            }
        }

        return res;

    }

    private int calWater(int[] height, int[] maxR, int l, int r) {
        int sum = 0;
        int leftMax = 0;
        for (int i = l; i <= r; ++i) {
            leftMax = Math.max(leftMax, height[i]);
            sum += Math.min(leftMax, maxR[i]) - height[i];
        }
        return sum;
    }
}