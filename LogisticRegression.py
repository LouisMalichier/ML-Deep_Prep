import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
  def sigmoid(z):
    return 1/(1+np.exp(-z))
  z = np.dot(X,weights)+bias
  z = np.dot(X,weights)+bias
  sig_z = sigmoid(z)
  return [1 if x>=0.5 else 0 for x in sig_z ]