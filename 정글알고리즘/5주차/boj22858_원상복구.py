import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))


order = []
for i in range(N):
    order.append([D[i], i])

order.sort()

new_card = [S[i] for i in range(N)]
for _ in range(K):
    tmp = []
    for d in order:
        tmp.append(new_card[d[1]])
    for i in range(N):
        new_card[i] = tmp[i]
print(*new_card)