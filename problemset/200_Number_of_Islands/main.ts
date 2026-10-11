function numIslands(grid: string[][]): number {
    
    let m = grid.length, n = grid[0].length;
    

    
    let visit: boolean[][] = [];
    for (let i = 0; i < m; ++i) {
        visit[i] = [];
        for (let j = 0; j < n; ++j) {
            visit[i][j] = false;
        }
    }
    
    let cnt = 0;

    const bfs = (grid: string[][], m: number, n: number, sr: number, sc: number, visit: boolean[][]) => {
        let dx = [0,0,1,-1];
        let dy = [1,-1,0,0];
        let q = [];
        q.push([sr, sc]);
        visit[sr][sc] = true;
        while (q.length > 0) {
            let f = q.shift();
            for (let i = 0; i < 4; ++i) {
                let x = f[0] + dx[i];
                let y = f[1] + dy[i];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == "1" && !visit[x][y]) {
                    visit[x][y] = true;
                    q.push([x, y]);
                }
            }
        }
    }
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] == "1" && visit[i][j] == false) {                
                bfs(grid, m, n, i , j, visit);
                cnt += 1;
            }
        }
    }
    
    return cnt;

    
};

