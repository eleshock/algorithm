import sys

input = sys.stdin.readline

def prod(mat1, mat2):
    n = len(mat1)
    new_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_mat[i][j] += mat1[i][k] * mat2[k][j]
    return new_mat

def remainder(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] %= 1000
    return mat

def operator(mat, b):
    if b == 1:
        return remainder(mat)
    elif b % 2 == 0:
        ans = operator(mat, b//2)
        return remainder(prod(ans, ans))
    else:
        ans = operator(mat, b//2)
        return remainder(prod(prod(ans, ans), mat))

n, b = map(int, input().split())
initial_matrix = [list(map(int, input().split())) for _ in range(n)]
remainder(initial_matrix)

ans = operator(initial_matrix, b)

for i in range(len(ans)):
    for j in range(len(ans)):
        print(ans[i][j], end = ' ')
    print()