from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
  count=0
  min=None
  for i in range(1,len(val_losses)):
    if min:
      if min-val_losses[i]<min_delta:
        count+=1
      else:
        min=val_losses[i]
        count=0
      if count == patience:
        return i,val_losses.index(min)
    else:
      if (val_losses[i-1]-val_losses[i])<min_delta:
        min=val_losses[i-1]
        count+=1
  return len(val_losses)-1,len(val_losses)-1