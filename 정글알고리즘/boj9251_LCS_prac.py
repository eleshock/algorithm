import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

n = len(string1)
m = len(string2)

LCS = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if string1[i] == string2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[n-1][m-1])