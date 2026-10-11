/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    // s.reverse();
    let right = s.length - 1;

    for (let left = 0; left < right; ++left, --right) {
        swap(s, left, right);
    }

};

function swap(s: string[], i: number, j: number) {
    let temp = s[i];
    s[i] = s[j];
    s[j] = temp;
}
