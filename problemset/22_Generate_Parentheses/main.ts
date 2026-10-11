function generateParenthesis(n: number): string[] {

    let result: string[] = [];
    
    generate(1, n * 2, 0, '', result);
    
    return result;
    
};

function generate(i: number, n: number, c: number, current: string, result: string[]) {
    
    if (i > n) {
        // console.log(c, current);
        if (c == 0) {
            result.push(current);
        }
        return;
    }
    
    if (c < 0) {
        return;
    }
    
    generate(i + 1, n, c + 1, current + '(', result);
    generate(i + 1, n, c - 1, current + ')', result);
}