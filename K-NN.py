import numpy as np
def k_nearest_neighbors(points, query_point, k):
    """
    Find k nearest neighbors to a query point
    
    Args:
        points: List of tuples representing points [(x1, y1), (x2, y2), ...]
        query_point: Tuple representing query point (x, y)
        k: Number of nearest neighbors to return
    
    Returns:
        List of k nearest neighbor points as tuples
    """
    def euclidean_distance(p1, p2):
        """
        Calculate Euclidean distance between two points
        """
        sum=0
        for dim in range(np.array(p1).shape[0]):
            sum += np.sum((np.array(p1[dim]) - np.array(p2[dim]))**2)
        return np.sqrt(sum)
    distance_to_querry=[]
    for point in points:
        distance_to_querry.append((euclidean_distance(query_point,point),point))
    distance_to_querry.sort(key=lambda x: x[0])
    return [p for _, p in distance_to_querry[:k]]
points = [(1, 2), (3, 4), (1, 1), (5, 6), (2, 3)]
query_point = (2, 2)
k = 3

k_nearest_neighbors(points,query_point,k)