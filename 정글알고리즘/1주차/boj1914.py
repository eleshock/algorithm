n = int(input())

# 하노이 탑 구현
def move(n, x, y):
    if n > 20: n = 20

    if n > 1:
        move(n-1, x, 6-x-y)
    
    print(x, y)
    
    if n > 1:
        move(n-1, 6-x-y, y)

# 과정 중에 n-1개의 원반을 2번 옮기고, 제일 아래 원반은 1번 옮김
def moveCount(n):
    if n == 1:
        return 1
    return 2 * moveCount(n-1) + 1

print(moveCount(n))

if n <= 20:
    move(n, 1, 3)