import numpy as np

a = np.random.randn(5)  # Creates a rank 1 array

print(np.dot(a, a.T)) # expecting an outer product, but got a number

a = np.random.randn(5, 1)
print(a)
print(a.T)

print(np.dot(a, a.T))

assert(a.shape == (5,1))
