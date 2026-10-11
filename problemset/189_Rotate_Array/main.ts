/**
 Do not return anything, modify nums in-place instead.
 */

 // O(1) space
function rotate(nums: number[], k: number): void {

    k = k % nums.length;

    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);

};

function reverse(nums: number[], start: number, end: number) {
    let temp: number;
    for (let i = start; i < end; ++i, --end) {
        temp = nums[i];
        nums[i] = nums[end];
        nums[end] = temp;
    }
}


function rotate_(nums: number[], k: number): void {

    let n = nums.length;
    let step = k % n;

    let start = n - step;
    // simple approach

    let other: number[] = [];
    for (let i = start; i < n; ++i) {
        other.push(nums[i]);
    }
    for (let i = n - 1; i >= step; --i) {
        nums[i] = nums[i - step];
    }
    for (let i = 0; i < step; ++i) {
        nums[i] = other[i];
    }

};



// rotate([1,2,3,4,5,6,7], 3);


rotate([1, 2, 3, 4, 5, 6, 7], 3);