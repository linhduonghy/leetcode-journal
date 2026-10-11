function permute(nums: number[]): number[][] {
    
    let permutes: number[][] = [];

    genPermutations(nums, 0, nums.length - 1, permutes);

    return permutes;
};

function genPermutations(nums: number[], l: number, r: number, permutes: number[][]) {

    if (l == r) {
        permutes.push(nums.slice());
        return;
    }

    for (let i = l; i <= r; ++i) {
        [nums[i], nums[l]] = [nums[l], nums[i]]; // swap i, l

        genPermutations(nums, l + 1, r, permutes);

        [nums[i], nums[l]] = [nums[l], nums[i]];
    }

}
