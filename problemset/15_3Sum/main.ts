function threeSum(nums: number[]): number[][] {
    let result = [];
    nums.sort((a, b) => a - b);
    let n = nums.length;
    for (let i = 0; i < n - 1; ++i) {       
        if (i > 0 && nums[i] == nums[i - 1]) 
            continue;
        let l = i + 1;
        let r = n - 1;
        while (l < r) {
            let sum = nums[i] + nums[l] + nums[r];
            if (sum == 0) {
                result.push([nums[i], nums[l], nums[r]]);
                ++l;
                while (l < r && nums[l] == nums[l - 1]) {
                    l++;
                }      
            } else if (sum < 0) {
                ++l;
            } else {
                --r;
            }
        }
    }
    
    return result;
};