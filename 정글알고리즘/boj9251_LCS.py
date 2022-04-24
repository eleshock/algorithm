import sys
input = sys.stdin.readline
# BOJ 9251
firstWord = input().strip()
secondWord = input().strip()

firstWordLength = len(firstWord)
secondWordLength = len(secondWord)

LCS = [[0] * (secondWordLength+1) for _ in range(firstWordLength+1)]

for i in range(1, firstWordLength+1):
    for j in range(1, secondWordLength+1):
        if firstWord[i-1] == secondWord[j-1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])