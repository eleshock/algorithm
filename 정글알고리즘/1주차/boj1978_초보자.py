# 초보자

import math
n = int(input())
a = list(map(int, input().split()))

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(n):
    if isPrime(a[i]):
        count += 1
print(count)