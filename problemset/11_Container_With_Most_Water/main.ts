function maxArea(height: number[]): number {

    let l = 0, r = height.length - 1;
    let result = 0;
    while (l < r) {
        if (height[l] < height[r]) { // 
            result = Math.max(height[l] * (r - l), result);
            ++l; 
        } else {
            result = Math.max(height[r] * (r - l), result);
            --r;
        }
    }
    return result;
};