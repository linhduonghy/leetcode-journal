function updateMatrix(mat: number[][]): number[][] {

    let m = mat.length;
    let n = mat[0].length;
    let d = [[0,1], [0,-1], [1,0], [-1,0]]; 
    
    let distance: number[][] = [];
    
    for (let i = 0; i < m; ++i) {
        distance[i] = [];
        for (let j = 0; j < n; ++j) {
            distance[i][j] = (m + n + 5);
        }
    }
    
    let q = [];
    
    for (let i = 0; i < m; ++i) 
        for (let j = 0; j < n; ++j) {
            if (mat[i][j] == 0) {
                distance[i][j] = 0;
                q.push([i, j]);
            }          
        }

    while (q.length > 0) {
        let f = q.shift();
        
        for (let i = 0; i < 4; ++i) {
            let x = f[0] + d[i][0];
            let y = f[1] + d[i][1];
            if (x >= 0 && x < m && y >= 0 && y < n && mat[x][y] == 1 && distance[x][y] > distance[f[0]][f[1]] + 1) {
                distance[x][y] = distance[f[0]][f[1]] + 1;
                q.push([x, y]);
            }
        }
    }
    return distance;
};

