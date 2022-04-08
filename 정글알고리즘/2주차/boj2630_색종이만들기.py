n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)] 

result = []

def dfs(size, x, y) :
    color = paper[x][y]
    for i in range(x, x + size) :
        for j in range(y, y + size) :
            if color != paper[i][j] :
                dfs(size//2, x, y)
                dfs(size//2, x, y + size//2)
                dfs(size//2, x + size//2, y)
                dfs(size//2, x + size//2, y + size//2)
                return
    if color == 0 :
        result.append(0)
    else :
        result.append(1)

dfs(n, 0, 0)

print(result.count(0))
print(result.count(1))