function fourSum(nums: number[], target: number): number[][] {

    let result: number[][] = [];

    // let uniqueResult: MySet<FourElement> = new MySet<FourElement>();
    const n = nums.length;
    
    for (let i = 0; i < n - 1; ++i) 
        for (let j = i + 1; j < n; ++j) 
            if (nums[i] > nums[j]) {
                let temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }

    let i = 0;
    while (i < n - 3) {     
        let j = n - 1;
        while (j > i + 2) {
            let k = i + 1, t = j - 1;
            while (k < t) {
                let sum = nums[i] + nums[j] + nums[k] + nums[t];
                if (sum == target) {
                    result.push([nums[i], nums[j], nums[k], nums[t]]);
                    // uniqueResult.add(new FourElement([nums[i], nums[j], nums[k], nums[t]]));
                    ++k; --t;
                    while (k < t && nums[k] == nums[k - 1]) ++k;
                    while (t > k && nums[t] == nums[t + 1]) --t;
                } else if (sum < target) {
                    ++k;
                } else {
                    --t;
                }
            }
            --j;
            while (j > i + 2 && nums[j] == nums[j + 1]) --j;
        }
        ++i;
        while (i < n - 3 && nums[i] == nums[i - 1]) ++i;
    }
    // console.log(result);
    return result;
};

// class MySet<T extends FourElement> extends Set<T> {
//     add(value: T): this {
//         let found = false;
//         for (let item of this) {
//             if (item.equals(value)) {
//                 found = true;
//                 break;
//             }
//         }
//         if (!found) {
//             super.add(value);
//         }
//         return this;
//     }
// }
// class FourElement {
//     elements!: number[];

//     constructor(arr: number[]) {
//         this.elements = arr;
//     }
//     equals(other: FourElement): boolean {
//         for (let i = 0; i < this.elements.length; ++i)
//             if (this.elements[i] != other.elements[i]) {
//                 return false;
//             }
//         return true;
//     }
// }
// fourSum([2, 2, 2, 2, 2], 8);