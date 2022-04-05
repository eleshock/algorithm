import time

a, b, v = map(int, input().split())

start = time.time()

snail = 0
count = 0
while v >= snail:
    snail += a
    count += 1
    if snail >= v:
        break
    snail -= b

print(count)

print("time : ", time.time() - start )