function reverseBits(n: number): number {
	
    let reverseNumber = 0;
    let p = 31;
    while (p >= 0) {
        reverseNumber |= ((n & 1) << p);
        n >>= 1;
        --p;
    }
    return reverseNumber;
};