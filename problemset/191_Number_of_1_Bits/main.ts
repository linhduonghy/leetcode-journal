function hammingWeight(n: number): number {
    
    let countBit1 = 0;
    while (n) {
        n = n & (n - 1); // set left bit 1 = 0
        countBit1 += 1;
    }
    return countBit1;
};