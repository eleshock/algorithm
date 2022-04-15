import sys
input = sys.stdin.readline

n = int(input())


def moo(acc, cur, n):
    prev = (acc-cur) // 2
    if n <= prev: return moo(prev, cur-1, n)
    elif n > prev + cur: return moo(prev, cur-1, n-prev-cur)
    else: return 'o' if n-prev-1 else 'm'

ㅌacc, k = 3, 0
while n > acc:
    k += 1
    acc = (acc * 2) + (k + 3)

print(moo(acc, k+3, n))