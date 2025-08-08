import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  numpy_array = np.array(list)
  numpy_array = numpy_array.reshape((3,3))

  #method 1
  mean_axis1 = np.mean(numpy_array, axis=0).tolist()
  mean_axis2 = np.mean(numpy_array, axis=1).tolist()
  mean_flat = np.mean(numpy_array).item()
  var_axis1 = np.var(numpy_array, axis=0).tolist()
  var_axis2 = np.var(numpy_array, axis=1).tolist()
  var_flat = np.var(numpy_array).item()
  std_axis1 = np.std(numpy_array, axis=0).tolist()
  std_axis2 = np.std(numpy_array, axis=1).tolist()
  std_flat = np.std(numpy_array).item()
  max_axis1 = np.max(numpy_array, axis=0).tolist()
  max_axis2 = np.max(numpy_array, axis=1).tolist()
  max_flat = np.max(numpy_array).item()
  min_axis1 = np.min(numpy_array, axis=0).tolist()
  min_axis2 = np.min(numpy_array, axis=1).tolist()
  min_flat = np.min(numpy_array).item()
  sum_axis1 = np.sum(numpy_array, axis=0).tolist()
  sum_axis2 = np.sum(numpy_array, axis=1).tolist()
  sum_flat = np.sum(numpy_array).item()

  calculations = {'mean': [mean_axis1,mean_axis2,mean_flat], 
                    'variance':[var_axis1,var_axis2,var_flat],
                    'standard deviation': [std_axis1, std_axis2, std_flat],
                    'max': [max_axis1,max_axis2,max_flat],
                    'min': [min_axis1, min_axis2, min_flat],
                    'sum': [sum_axis1, sum_axis2, sum_flat]}
    #method 2
  calculations = {}
  Statistics = {
     'mean': np.mean,
     'variance': np.var,
     'standard deviation': np.std,
     'max': np.max,
     'min': np.min,
     'sum': np.sum,      
    }
  for name, oparation in Statistics.items():
      calculations[name] = [oparation(numpy_array, axis = 0).tolist(), oparation(numpy_array, axis = 1).tolist(), oparation(numpy_array).item()]



  return calculations
