function rob(nums: number[]): number {

    if (nums.length == 1) {
        return nums[0];
    }
    if (nums.length == 2) {
        return Math.max(nums[0], nums[1]);
    }
    
    let money: number[] = [];
    
    money[0] = nums[0];
    money[1] = Math.max(nums[1], nums[0]);
    
    for (let i = 2; i < nums.length; ++i) {
        
        money[i] = Math.max(money[i - 2] + nums[i], money[i - 1]);
        // console.log(i, money[i]);
    }
    return money[nums.length - 1];

};