import numpy as np
import time
import math

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


## Exponential operation on vector
# for loop version
n = 5
u = np.zeros((n, 1))
for i in range(n):
    u[i] = math.exp(u[i])
# vectorized version
n = 5
u = np.zeros((n, 1))
u = np.exp(u)


## Logistic regression derivatives
