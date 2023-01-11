import time

pt = 0
ct = 0
dt = 0

a = int(input())
v = 0

bo=time.time()

while(True):
    pt = ct
    ct = time.time()
    dt = (ct - pt)
    v += a * dt

    print(v -bo)
