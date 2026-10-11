function numSubarrayProductLessThanK(nums: number[], k: number): number {

    let l = 0
    
    while (l < nums.length && nums[l] >= k) {
        ++l;
    }
    let r = l;    
    let acc = 1;
    while (r < nums.length && acc * nums[r] < k) {
        acc *= nums[r];
        ++r;
    }
    --r;
    
    let count = (r - l + 1) * (r - l + 2) >> 1;
    while (r < nums.length - 1) {
        ++r;
        if (nums[r] >= k) {            
            ++r;
            l = r;
            acc = 1;
            continue;
        }
        acc *= nums[r];
        // console.log(acc);
        while (l < r && acc >= k) {
            acc /= nums[l];
            ++l;
        }
        // console.log(acc, l, r);        
        count += (r - l + 1);
    }
    return count;
};

