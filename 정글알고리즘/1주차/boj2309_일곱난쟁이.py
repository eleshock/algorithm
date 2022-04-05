from itertools import combinations

arr = [int(input()) for _ in range(9)]

nanjangcom = list(combinations(arr, 7))

for nanjangs in nanjangcom:
    if sum(nanjangs) == 100:
        a = list(nanjangs)
        a.sort()
        for i in a:
            print(i)
        break