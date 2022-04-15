import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
setWords = list(set(words))
setWords.sort()


arr = [[] for _ in range(51)]
for word in setWords:
    for i in range(len(arr)):
        if len(word) == i:
            arr[i].append(word)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if len(arr[i]) >= 1:
            print(arr[i][j])