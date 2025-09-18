import numpy as np
def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
  final_centroids = initial_centroids
  
  def assign_labels(points):
      labels = []
      for point in points:
        distances = [np.linalg.norm(np.array(point) - np.array(c)) for c in final_centroids]
        labels.append(np.argmin(distances))
      return np.array(labels)

  def centroid_calculation(points,labels):
    points = np.array(points)
    final_centroids = np.array([points[labels == i].mean(axis=0) for i in range(k)])
    return final_centroids
    
  for _ in range(max_iterations):
    labels = assign_labels(points)
    print(labels)
    final_centroids = centroid_calculation(points,labels)
  return final_centroids

points = [(0, 0), (1, 0), (0, 1), (1, 1), (5, 5), (6, 5), (5, 6), (6, 6),(0, 5), (1, 5), (0, 6), (1, 6), (5, 0), (6, 0), (5, 1), (6, 1)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10

k_means_clustering(points=points,k=k,initial_centroids=initial_centroids,max_iterations=max_iterations)