function orangesRotting(grid: number[][]): number {

    let m = grid.length;
    let n = grid[0].length;
    let d = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let steps: number[][] = [];
    let q = [];

    for (let i = 0; i < m; ++i) {
        steps[i] = [];
        for (let j = 0; j < n; ++j) {
            steps[i][j] = 10000;
            if (grid[i][j] == 2) {
                steps[i][j] = 0;
                q.push([i, j]);
            }
        }
    }

    let result = 0;

    while (q.length > 0) {
        let f = q.shift();
        for (let i = 0; i < 4; ++i) {
            let x = f[0] + d[i][0];
            let y = f[1] + d[i][1];
            
            if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] != 0 && steps[x][y] > steps[f[0]][f[1]] + 1) {
                
                steps[x][y] = steps[f[0]][f[1]] + 1;
                grid[x][y] = 2;
                result = Math.max(result, steps[x][y]);
                q.push([x, y]);
            }
        }
    }
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] == 1) {
                // console.log(i, j, steps[i][j]);
                return -1;
            }
        }
    }
    return result;
};
