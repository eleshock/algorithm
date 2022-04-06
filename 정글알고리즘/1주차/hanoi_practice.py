n = int(input())

def move(n, x, y):
    if n > 20: n = 20
    
    if n > 1:
        move(n-1, x, 6-x-y)

    print(x, y)
        
    if n > 1:    
        move(n-1, 6-x-y, y)

def moveCount(n):
    if n == 1:
        return 1
    return 2 * moveCount(n-1) + 1

print(moveCount(n))

if n <= 20:
    move(n, 1, 3)