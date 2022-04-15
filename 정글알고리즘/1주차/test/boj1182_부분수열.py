from itertools import combinations

n, s = map(int, input().split())

initial= list(map(int, input().split()))

count = 0

for i in range(1, n+1):
    partials = list(combinations(initial, i))
    for partial in partials:
        if sum(partial) == s:
            count += 1

print(count)