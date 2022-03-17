import random as rn
import time

rn.seed(1)
start = time.time()
for i in range(1000):
    a = rn.randint(0, 20)
    a = a << 5
    (a)
time1 = time.time() - start
start = time.time()
rn.seed(1)
for i in range(1000):
    a = rn.randint(0, 20)
    a = a * (32)
    print(a)
time2 = time.time() - start
print(time1)
print(time2)
