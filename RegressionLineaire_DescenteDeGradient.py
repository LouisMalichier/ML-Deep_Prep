import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
  m, n = X.shape
  theta = np.zeros((n, 1))  # vecteur colonne
  y = y.reshape(-1, 1)      # vecteur colonne

  for _ in range(iterations):
      predictions = X.dot(theta)            # (m,1)
      error = predictions - y               # (m,1)
      gradient = (1/m) * X.T.dot(error)     # (n,1)
      theta = theta - alpha * gradient      # update

  return theta

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

linear_regression_gradient_descent(X=X,y=y,alpha=alpha,iterations=iterations)

