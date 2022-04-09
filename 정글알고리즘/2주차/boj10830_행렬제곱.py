import sys

def remainder(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] %= 1000

def prod(matrix1, matrix2):
    n = len(matrix1)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    remainder(new_matrix)
    return new_matrix

def division(matrix, b):
    if b == 1:
        return matrix
    elif b % 2 == 0:
        m = division(matrix, b//2)
        return prod(m, m)
    else:
        m = division(matrix, b // 2)
        return prod((prod(m, m)), matrix)

input = sys.stdin.readline
n, b = map(int, input().split())

initial_matrix = [list(map(int, input().split())) for _ in range(n)]
remainder(initial_matrix)

ans = division(initial_matrix , b)

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = ' ')
    print()