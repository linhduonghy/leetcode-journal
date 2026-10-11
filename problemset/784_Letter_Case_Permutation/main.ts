function letterCasePermutation(s: string): string[] {
    
    let permutations: string[] = [];

    genletterCasePermutation(s, 0, permutations);

    return permutations;
};

function genletterCasePermutation(s: string, count: number, permutations: string[]) {
    if (count == s.length) {
        permutations.push(s);
        return;
    }

    if (s.charAt(count) >= '0' && s.charAt(count) <= '9') {
        genletterCasePermutation(s, count + 1, permutations);
    } else {
        s = s.substr(0, count) + s.charAt(count).toLowerCase() + s.substr(count + 1);
        genletterCasePermutation(s, count + 1, permutations);
        s = s.substr(0, count) + s.charAt(count).toUpperCase() + s.substr(count + 1);
        genletterCasePermutation(s, count + 1, permutations);
    }
    
}

