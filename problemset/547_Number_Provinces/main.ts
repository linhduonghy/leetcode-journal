function findCircleNum(isConnected: number[][]): number {

    let n = isConnected.length;

    let visit: boolean[] = [];
    for (let i = 0; i < n; ++i)
        visit[i] = false;

    let numOfProvinces = 0;

    for (let i = 0; i < n; ++i)
        if (!visit[i]) {
            dfs(isConnected, n, i, visit);
            ++numOfProvinces;
        }

    function dfs(g: number[][], n: number, sr: number, visit: boolean[]) {
        visit[sr] = true;
        for (let i = 0; i < n; ++i)
            if (!visit[i] && g[sr][i] == 1)
                dfs(g, n, i, visit);
    }
    return numOfProvinces;
};
