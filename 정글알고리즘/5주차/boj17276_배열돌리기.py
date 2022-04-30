# 1시간 20분 소요
# 고칠 것이 너무 많고 계산복잡도상으로 비효율적인 코드

import copy
import sys
input = sys.stdin.readline

def clockwise(matrix, n, d):
    new_matrix = copy.deepcopy(matrix)
    count = abs(d//45)
    for _ in range(count):
        for i in range(n):
            new_matrix[i][n//2] = matrix[i][i]  
            new_matrix[i][n-1-i] = matrix[i][n//2]
            new_matrix[n//2][n-1-i] = matrix[i][n-1-i] 
            new_matrix[i][i] = matrix[n//2][i]
        matrix = copy.deepcopy(new_matrix)
    return new_matrix

def counterClockwise(matrix, n, d):
    new_matrix = copy.deepcopy(matrix)
    count = abs(d//45)
    for _ in range(count):
        for i in range(n):
            new_matrix[n//2][i] = matrix[i][i]
            new_matrix[i][n-1-i] = matrix[n//2][n-1-i]
            new_matrix[i][n//2] = matrix[i][n-1-i]
            new_matrix[i][i] = matrix[i][n//2]
        matrix = copy.deepcopy(new_matrix)
    return new_matrix

T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    if d > 0:
        ans = clockwise(matrix, n, d)
        for i in ans:
            print(*i)
    elif d < 0:
        ans = counterClockwise(matrix, n, d)
        for i in ans:
            print(*i)
    else:
        for i in matrix:
            print(*i)