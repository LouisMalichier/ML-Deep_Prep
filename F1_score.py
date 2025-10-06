def calculate_f1_score(y_true, y_pred):
  TP = [1 if (y_true[i] == y_pred[i] and y_true[i]==1) else 0 for i in range(len(y_true))]
  FP = [1 if (y_true[i] != y_pred[i] and y_pred[i]==1) else 0 for i in range(len(y_true))]
  FN = [1 if (y_true[i] != y_pred[i] and y_pred[i]==0) else 0 for i in range(len(y_true))]

  if (sum(TP)+sum(FP)) == 0 or (sum(TP)+sum(FN)) == 0 :
    return 0.0
  precision = sum(TP)/(sum(TP)+sum(FP))
  recall = sum(TP)/(sum(TP)+sum(FN))

  f1=2*(precision*recall)/(precision+recall)
  return round(f1,3)
