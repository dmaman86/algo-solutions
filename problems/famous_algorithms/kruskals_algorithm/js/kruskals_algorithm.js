export const kruskalsAlgorithm = (() => {
  const find = (parent, x) => {
    if (parent[x] !== x) {
      parent[x] = find(parent, parent[x]);
    }
    return parent[x];
  };

  const unionSets = (parent, rank, x, y) => {
    const rootX = find(parent, x);
    const rootY = find(parent, y);

    if (rootX !== rootY) {
      if (rank[rootX] > rank[rootY]) {
        parent[rootY] = rootX;
      } else if (rank[rootX] < rank[rootY]) {
        parent[rootX] = rootY;
      } else {
        parent[rootY] = rootX;
        rank[rootX] += 1;
      }
      return true;
    }
    return false;
  };

  return (edges) => {
    const allEdges = [];

    for (let u = 0; u < edges.length; u++) {
      for (const edge of edges[u]) {
        const [v, w] = edge;
        if (u < v) {
          allEdges.push([w, u, v]);
        }
      }
    }
    allEdges.sort((a, b) => a[0] - b[0]);

    const parent = Array.from({ length: edges.length }, (_, i) => i);
    const rank = Array(edges.length).fill(0);
    const mst = Array.from({ length: edges.length }, () => []);

    for (const [w, u, v] of allEdges) {
      if (unionSets(parent, rank, u, v)) {
        mst[u].push([v, w]);
        mst[v].push([u, w]);
      }
    }

    for (let i = 0; i < edges.length; i++) {
      mst[i].sort((a, b) => a[0] - b[0]);
    }
    return mst;
  };
})();
