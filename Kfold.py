import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    fold_size = len(X)//k
    reste = len(X)%k

    indices = np.arange(len(X))

    if shuffle:
      np.random.shuffle(indices)
    
    output=[]
    start_idx = 0
    for fold in range(k-1):
      end_idx = start_idx+fold_size+(1 if fold<reste else 0)
      test=indices[start_idx:end_idx].tolist()
      current_fold = np.concatenate([indices[:start_idx],indices[end_idx:]]).tolist()
      output.append((current_fold,test))
      start_idx=end_idx

    return output

k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=6, shuffle=True)
