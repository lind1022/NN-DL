import numpy as np
import time

# Vectorized version

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print("Vectorized version:" + str(10000*(toc-tic)) + "ms")

# For loop version
c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print("For loop:" + str(10000*(toc-tic)) + "ms")
