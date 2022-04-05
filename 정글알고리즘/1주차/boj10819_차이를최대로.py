from itertools import permutations

n = int(input())

a = list(map(int, input().split()))

arrays = list(permutations(a))

arrSum = []

for array in arrays:
    result = 0
    for j in range(n-1):
        result += abs(array[j]-array[j+1])
    arrSum.append(result)

print(max(arrSum))