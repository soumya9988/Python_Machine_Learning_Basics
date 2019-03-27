import numpy as np

weight_kg = [60.9, 35, 76.4, 2.80, 67.14]
np_weight_kg= np.array(weight_kg)
np_weight_lb = np_weight_kg * 2.2
print(np_weight_lb)