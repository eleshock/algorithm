from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

cards = list(map(int, input().rstrip().split()))

arr = list(combinations(cards, 3))

cards_sums = [sum(arr[i]) for i in range(len(arr))]

cards_sums.sort(reverse=True)

for cards_sum in cards_sums:
    if cards_sum <= m:
        print(cards_sum)
        break