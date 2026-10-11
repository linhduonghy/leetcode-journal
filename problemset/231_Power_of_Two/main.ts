function isPowerOfTwo(n: number): boolean {

    if (n < 1) {
        return false;
    }

    while (n > 1) {
        if ((n & 1) == 1) {
            return false;
        }
        n /= 2;
    }

    return true;
};