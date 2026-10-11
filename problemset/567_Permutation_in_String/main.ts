function checkInclusion(s1: string, s2: string): boolean {

    let count: number[] = [];
    
    let n1 = s1.length, n2 = s2.length;
    
    for (let i = 0; i < 26; ++i) {
        count[i] = 0;
    }
    
    let aCode = 'a'.charCodeAt(0);
    for (let i = 0; i < n1; ++i) {
        ++count[s1.charCodeAt(i) - aCode];
    }
    
    let count1: number[][] = [];
    
    for (let i = 0; i < n2; ++i) {
        count1[i] = [];
        for (let j = 0; j < 26; ++j) {
            count1[i][j] = 0;
        }        
    }
    count1[0][s2.charCodeAt(0) - aCode] = 1;
    for (let i = 1; i < n2; ++i) {
        for (let j = 0; j < 26; ++j) {
            count1[i][j] = count1[i - 1][j] + (s2.charCodeAt(i) - aCode == j ? 1 : 0);
        }        
    }
    for (let i = 0; i < n2 - n1 + 1; ++i) {
        
        if (matches(count, count1, i, i + n1 - 1)) {
            return true;
        }
    }
    return false;
};

function matches(count: number[], count1: number[][], l: number, r: number) {
    for (let i = 0; i < 26; ++i) {
        if (count[i] != get(count1, i, l, r)) {
            return false;
        }
    }
    return true;
}

function get(count1: number[][], i: number, l: number, r: number) {
    if (l == 0) {
        return count1[r][i];
    } else {
        return count1[r][i] - count1[l - 1][i];
    }
}