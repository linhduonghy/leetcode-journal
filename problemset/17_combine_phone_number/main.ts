function letterCombinations(digits: string): string[] {

    
    let result: string[] = [];

    if (digits.length == 0) {
        return result;
    }
    
    let chars: string = '';
    for (let x = 0; x < 26; ++x) {
        chars = chars + String.fromCharCode(x + 97);
    }
    
    let map: string[] = [];
    let i = 0;
    for (let x = 0; x < 8; ++x) {
        if (x == 5 || x == 7) {
            map[x] = chars.substr(i, 4);
            i += 4;
        } else {
            map[x] = chars.substr(i, 3);
            i += 3;
        }        
    }

    let s: string[] = [];
    for (i = 0; i < digits.length; ++i) {
        // convert char to number
        let x = digits.charCodeAt(i) - 48;
        
        // push target chars to s
        s.push(map[x - 2]);        
    }
    
    Try(s, result, 0);
    return result;

};

function Try(s: string[], result: string[], i: number, prev: string = '') {

    if (i == s.length - 1) {
        for (let j = 0; j < s[i].length; ++j) {
            result.push(prev + s[i][j]);
        }
        return;
    }

    for (let j = 0; j < s[i].length; ++j) {
        Try(s, result, i + 1, prev + s[i][j]);
    }
}
