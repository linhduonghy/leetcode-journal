function climbStairs(n: number): number {

    //     let steps: number[] = [];
    //     steps[0] = 1;
    //     steps[1] = 1;
    //     for (let i = 2; i <= n; ++i) {
    //         steps[i] = steps[i - 1] + steps[i - 2];
    //     }
        
    //     return steps[n];
        
        if (n == 1) {
            return 1;
        }
        let c0 = 1;
        let c1 = 1;
        let steps: number;
        let i = 2;
        while (i <= n) {
            steps = c0 + c1;
            c0 = c1;
            c1 = steps;
            ++i;
        }
        return steps;
    };