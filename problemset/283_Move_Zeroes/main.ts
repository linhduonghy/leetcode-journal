/**
 Do not return anything, modify nums in-place instead.
 */
 function moveZeroes(nums: number[]): void {

    let n = nums.length;
    let cnt = 0;
    for (let i = 0; i < n; ++i) {
        if (nums[i] != 0) {
            nums[cnt] = nums[i];
            ++cnt;
        }
    }

    for (let i = cnt; i < n; ++i) {
        nums[i] = 0;
    }

    
};