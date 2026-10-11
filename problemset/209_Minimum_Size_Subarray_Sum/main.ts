function minSubArrayLen(target: number, nums: number[]): number {
    // solution 1: binary search O(nlogn) 
    // return sol1(target, nums);
    
    // solution 2: Two point: O(n)
    return sol2(target, nums);
};

function sol2(target:number, nums: number[]) {
    let sum = 0;
    let res = nums.length + 1;
    let left = 0;
    for (let right = 0; right < nums.length; ++right) {
        sum += nums[right];
        // maintain sum < target
        while (sum >= target) {
            res = Math.min(res, right - left + 1);            
            sum -= nums[left];
            ++left;
        }
    }
    
    return (res == nums.length + 1) ? 0 : res;
}

function sol1(target: number, nums: number[]) {
    
    let sum: number[] = [];
    
    sum[0] = nums[0];
    for (let i = 1; i < nums.length; ++i) {
        sum[i] = sum[i - 1] + nums[i];
    }
    
    let result = sum.length + 1;
    
    for (let i = 0; i < sum.length; ++i) {
        let l = i, r = sum.length - 1;
        
        
        while (l <= r) {
            let mid = (l + r) >> 1;
            if (calSum(sum, i, mid) < target) {
                l = mid + 1;
            } else {
                result = Math.min(result, mid - i + 1);
                r = mid - 1;
            }
        }
    }
    return (result == sum.length + 1) ? 0 : result;
 }
    
function calSum(sum: number[], l: number, r: number) {
    if (!l) {
        return sum[r];
    }
    return sum[r] - sum[l - 1];
}