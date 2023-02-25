import numpy as np
import functions as f
a = np.array([1,2,3])
b = np.delete(a, [])

total_dict = {}
total_dict['1'] = a
total_dict['2'] = []
total_dict['2'] = b
print(total_dict['1'][0])

skip = [1,2,3]

flux = total_dict['2']
flux_new = np.delete(flux, 2)
print([x for x in np.delete(total_dict['1'], [])])