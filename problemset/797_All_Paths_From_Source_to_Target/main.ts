function allPathsSourceTarget(graph: number[][]): number[][] {

    let n = graph.length;
    let result: number[][] = [];
    
    dfs(0, n - 1, graph, [0], result);
    
    return result;
};

function dfs(src: number, dst: number, graph: number[][], trace: number[], result: number[][]) {
    if (src == dst) {
        result.push(trace.slice(0));
        return;
    }        
    for (let adj of graph[src]) {
        trace.push(adj);
        dfs(adj, dst, graph, trace, result);
        trace.pop();
    }
}
