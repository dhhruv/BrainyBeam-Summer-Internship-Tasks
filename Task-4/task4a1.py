import numpy as np

# method-1: array in NumPy
ar = np.array([["n", "u", "m", "p", "y"], ["n", "u", "m", "p", "y"]])
print("Array:\n{}".format(ar))

# method-2: Universal function in NumPy
n = np.array([0, np.pi / 2, np.pi])
print(
    "Sine Values: {}".format(np.sin(n))
)  # will print the sine values of specified list

# method-3: all() in NumPy
print(
    "True for axis-0? {}".format(np.all([[True, True], [True, True]], axis=0))
)  # will return if every element is True for  given axis or not

# method-4: argsort() in NmuPy
print(
    "Indices for sorted array: \n{}".format(np.argsort(ar))
)  # returns the indices that would sort the array

# method-5: fill() in NumPy
n.fill(0)
print("Filled array: {}".format(n))  # will fill the entire array with specified value
