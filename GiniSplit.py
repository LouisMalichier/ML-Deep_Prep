import numpy as np
from typing import Tuple

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    n_samples, n_features = X.shape

    def gini(labels: np.ndarray) -> float:
        N_subset = len(labels)
        if N_subset == 0:
            return 0.0
        _, counts = np.unique(labels, return_counts=True)
        probs = counts / N_subset
        return 1.0 - np.sum(probs ** 2)

    best_gini = float('inf')
    best_feature, best_threshold = None, None

    for feature in range(n_features):
        thresholds =  np.unique(X[:, feature]) # On considere chaque valeune unique comme un seuil candidat et pas les milieux entre 2 points consécutif
        for s in thresholds:
            left = X[:, feature] <= s
            right = X[:, feature] > s

            G_left = gini(y[left])
            G_right = gini(y[right])

            G_split = (np.sum(left)/n_samples) * G_left + (np.sum(right)/n_samples) * G_right

            if G_split < best_gini:
                best_gini = G_split
                best_feature = feature
                best_threshold = s

    return best_feature, best_threshold

# Test
X1 = np.array([[2.5], [3.5], [1.0], [4.0]]) 
y1 = np.array([0, 1, 0, 1])
f, t = find_best_split(X1, y1)
print(f, t)
