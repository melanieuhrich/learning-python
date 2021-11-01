# numpy arrays --
    # -- great alternatives to Python lists
    # -- fast, easy to work with
    # -- allow us to perform calculations across entire arrays



# lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# import the numpy package as np
import numpy as np 

# create 2 numpy arrays from height and weight 
np_height = np.array(height)
np_weight = np.array(weight)

# prints <class 'numpy.ndarray'>
print(type(np_height))



# element-wise calculations 

# calculate bmi 
bmi = np_weight / np_height ** 2



# subsetting

# for a boolean response 
bmi > 23

# print only those observations above 23
bmi[bmi > 23]



# exercise

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)