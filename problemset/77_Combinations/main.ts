function combine(n: number, k: number): number[][] {

    let comb: number[][] = [];
    let used: boolean[] = [];

    for (let i = 0; i <= n; ++i) used[i] = false;

    gen(n, k, 0, [], used, comb);
    
    return comb;
};

function gen(n: number, k: number, count: number, current: number[], used: boolean[], comb: number[][]) {
    if (count == k) {
        comb.push(current.slice());
        return;
    }

    let start = count == 0 ? 1 : current[count - 1] + 1;
    for (let i = start; i <= n; ++i) {
        if (used[i] == false) {            
            current.push(i);
            used[i] = true;      
            gen(n, k, count + 1, current, used, comb);
            current.pop();
            used[i] = false;
        }
    }

}



