export const primsAlgorithm = (edges) => {
  const inMST = new Array(edges.length).fill(false);
  const mstEdges = Array.from({ length: edges.length }, () => []);
  const minHeap = [[0, 0, -1]];

  while (minHeap.length) {
    minHeap.sort((a, b) => a[0] - b[0]);
    const [weight, currentNode, parentNode] = minHeap.shift();

    if (inMST[currentNode]) continue;
    inMST[currentNode] = true;

    if (parentNode !== -1) {
      mstEdges[currentNode].push([parentNode, weight]);
      mstEdges[parentNode].push([currentNode, weight]);
    }
    for (const [neighbor, edgeWeight] of edges[currentNode]) {
      if (!inMST[neighbor]) {
        minHeap.push([edgeWeight, neighbor, currentNode]);
      }
    }
  }
  return mstEdges;
};
