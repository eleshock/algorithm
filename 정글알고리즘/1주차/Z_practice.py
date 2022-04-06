import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

count = 0

def recursive(size, x, y):
    global count
    if x == r and y == c:
        print(count)
        return

    if size == 1:
        count += 1
        return
    
    if not (x <= r < x + size and y <= c < y + size):
        count += size * size
        return
    
    recursive(size//2, x, y)
    recursive(size//2, x, y + size//2)
    recursive(size//2, x + size//2, y)
    recursive(size//2, x + size//2, y + size//2)

recursive(2**n, 0, 0)
