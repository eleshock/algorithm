import sys
input = sys.stdin.readline

def find(word):
    keyboard = [
        ['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l'],
        ['z','x','c','v','b','n','m']
    ]

    for i, key in enumerate(keyboard):
        if word in key:
            y = i
            x = key.index(word)
            return x, y


l, r = map(str, input().rstrip().split())
data = input().rstrip()
result = 0

# 한글 자음의 위치에 있는 영문자 저장
consonant = "qwertasdfgzxcv"

for d in data:
    
    # 이미 왼손이나 오른손이 그 위치에 있는경우
    if l == d or r == d:
        result += 1
        
    
    # 아닌 경우 각각의 위치 별 x, y위치를 입력받자.
    else:

        lx, ly = find(l)
        rx, ry = find(r)
        dx, dy = find(d)

        # 자음이라면 왼쪽이 이동한다.
        if d in consonant:
            result += abs(lx-dx) + abs(ly-dy) + 1
            l, lx, ly = d, dx, dy
        # 모음이라면 오른쪽이 이동한다.
        else:
            result += abs(rx-dx) + abs(ry-dy) + 1
            r, rx, ry = d, dx, dy

print(result)