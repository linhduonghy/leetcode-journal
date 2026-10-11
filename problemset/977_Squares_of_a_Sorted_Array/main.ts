
function sortedSquares(nums: number[]): number[] {

    // // propagate from min value
    // let n = nums.length;

    // let result: number[] = [];
    // let minId = 0;

    // for (let i = 0; i < n; ++i) {
    //     if (nums[i] < 0) {
    //         nums[i] = -nums[i];
    //     }
    // }    

    // for (let i = 1; i < n; ++i) {
    //     if (nums[i] < nums[minId]) {
    //         minId = i;
    //     }
    // }

    // result.push(nums[minId] * nums[minId]);
    // let l = minId - 1, r = minId + 1;
    // while (l >= 0 && r < n) {
    //     if (nums[l] < nums[r]) {
    //         result.push(nums[l] * nums[l]);
    //         --l;
    //     } else {
    //         result.push(nums[r] * nums[r]);
    //         ++r;
    //     }
    // }
    // while (l >= 0) {
    //     result.push(nums[l] * nums[l]);
    //     --l;
    // }
    // while (r < n) {
    //     result.push(nums[r] * nums[r]);
    //     ++r;
    // }    
    // return result;

    // propagate from max value
    let l = 0, r = nums.length - 1;
    let result: number[] = [];
    for (let i = nums.length - 1; i >= 0; --i) {

        if (nums[l] * nums[l] > nums[r] * nums[r]) {
            result[i] = nums[l] * nums[l];
            ++l;
        } else {
            result[i] = nums[r] * nums[r];
            --r;
        }
    }
    return result;
};

console.log(sortedSquares([-5,-3,-2,-1]));