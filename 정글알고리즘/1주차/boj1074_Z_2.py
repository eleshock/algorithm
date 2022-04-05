import sys
input = sys.stdin.readline

def recursive(size, x , y):
    global count
    if x == r and y == c:
        print(count)
        return

    if size == 1:
        count += 1
        return
    if not (x <= r < x+size and y <= c < y + size):
        count += size * size
        return
    
    recursive(size//2, x, y)
    recursive(size//2, x, y + size//2)
    recursive(size//2, x + size//2, y)
    recursive(size//2, x + size//2, y + size//2)

n, r, c = map(int, input().split())

count = 0
recursive(2**n, 0, 0)

# 분할 정복
# size가 1이 될 때까지 잘라서 r, c를 찾을 때까지 더해준 다음 print
# 하지만 목표한 값을 print 하더라도 남아있는 재귀는 끝까지 멈출 수 없다는 점에서 비효율적