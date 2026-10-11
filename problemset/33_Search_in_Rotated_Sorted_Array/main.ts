function search(nums: number[], target: number): number {
    return bSearch(nums, 0, nums.length - 1, target);
};

function bSearch(nums: number[], l: number, r: number, target: number) {
    if (l == r) {
        if (nums[l] == target) {
            return l;
        }
        return -1;
    }
    
    let mid = (l + r) >> 1;
    let sLeft = bSearch(nums, l, mid, target);
    let sRight = bSearch(nums, mid + 1, r, target);
    
    if (sLeft == -1 && sRight == -1) {
        return -1;
    }
    if (sLeft == -1) {
        return sRight;
    }
    return sLeft;
}