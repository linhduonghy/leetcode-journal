function search(nums: number[], target: number): number {
    let l = 0, r = nums.length - 1;
    
    while (l <= r) {
        let mid = (l + r) >> 0;
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[mid] > target) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return -1;
};

console.log(search([-1,0,3,5,9,12], 9));