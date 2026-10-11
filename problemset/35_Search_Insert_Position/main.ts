function searchInsert(nums: number[], target: number): number {

    let l = 0, r = nums.length - 1, result = r + 1;

    while (l <= r) {
        let mid = (l + r) >> 1;
        if (nums[mid] >= target) {
            result = mid;
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }

    return result;
};