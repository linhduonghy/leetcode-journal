function singleNumber(nums: number[]): number {
    for (let i = 0; i < nums.length - 1; ++i) {
        nums[i + 1] ^= nums[i];
    }
    return nums[nums.length - 1];
};