import { MinPriorityQueue } from "@datastructures-js/priority-queue";

export const dijkstrasAlgorithm = (() => {
  const initDistanceAndQueue = (start, n, distances, pq) => {
    distances.length = n;
    distances.fill(Infinity);
    distances[start] = 0;
    pq.enqueue({ element: start, priority: 0 });
  };

  const relaxEdges = (currentVertex, currentDistance, edges, pq, distances) => {
    if (!Array.isArray(edges[currentVertex])) return;

    for (const edge of edges[currentVertex]) {
      const [vertex, weight] = edge;

      const newDistance = currentDistance + weight;

      if (newDistance < distances[vertex]) {
        distances[vertex] = newDistance;
        pq.enqueue({ element: vertex, priority: newDistance });
      }
    }
  };

  const dijkstra = (start, edges, distances) => {
    const n = edges.length;
    const pq = new MinPriorityQueue();

    initDistanceAndQueue(start, n, distances, pq);

    while (!pq.isEmpty()) {
      const { element: currentVertex, priority: currentDistance } =
        pq.dequeue();
      if (currentDistance > distances[currentVertex]) continue;

      relaxEdges(currentVertex, currentDistance, edges, pq, distances);
    }
  };

  const convertUnreachableToNegativeOne = (distances) => {
    for (let i = 0; i < distances.length; i++) {
      if (distances[i] === Infinity) distances[i] = -1;
    }
  };

  return (start, edges) => {
    const distances = [];
    dijkstra(start, edges, distances);
    convertUnreachableToNegativeOne(distances);
    return distances;
  };
})();
