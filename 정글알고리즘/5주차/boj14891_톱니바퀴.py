import sys

def findRotatingGear(target, direction): # 회전 시킬 톱니바퀴를 찾는 함수
    global gears
    res = [0] * 4

    res[target] = direction
    
    # target을 기준으로 왼쪽 검사
    for i in range(target-1, -1, -1):
        if gears[i][2] == gears[i+1][6]:
            break
        
        res[i] = res[i+1] * -1

    # target을 기준으로 오른쪽 검사
    for i in range(target+1, 4):
        if gears[i][6] == gears[i-1][2]:
            break

        res[i] = res[i-1] * -1
    
    return res

def rotate(res): # 톱니바퀴를 회전 시키는 함수
    global gears

    for i in range(4):
        if res[i] == 0: # 해당 톱니바퀴는 회전시키지 않는다.
            continue

        elif res[i] == 1: # 해당 톱니바퀴는 시계 방향으로 회전시킨다.
            gears[i] = [gears[i][7]] + gears[i][0:7]

        else: # 해당 톱니바퀴는 시계 반대 방향으로 회전시킨다.
            gears[i] = gears[i][1:8] + [gears[i][0]]
            
    

gears = [ list(map(int, list(sys.stdin.readline().strip()))) for _ in range(4) ]

k = int(sys.stdin.readline().strip())

rotatingInfo = [ tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(k) ]

for g, d in rotatingInfo:
    res = findRotatingGear(g-1, d)
    rotate(res)


score = gears[0][0] + gears[1][0] * 2 + gears[2][0] * 4 + gears[3][0] * 8

print(score)