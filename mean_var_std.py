import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  
  matrix = np.array(
    [[list[0],list[1], list[2]],
    [list[3],list[4],list[5]],
    [list[6],list[7],list[8]]])
  
  calculations = {
    'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.flatten().mean()],
    'variance': [np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(matrix)],
    'standard deviation': [np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(matrix)],
    'max':[np.max(matrix, axis=0).tolist(),np.max(matrix, axis=1).tolist(),np.max(matrix)],
    'min':[np.min(matrix, axis=0).tolist(),np.min(matrix, axis=1).tolist(),np.min(matrix)],
    'sum':[np.sum(matrix, axis=0).tolist(),np.sum(matrix, axis=1).tolist(),np.sum(matrix)]
  }

  return calculations