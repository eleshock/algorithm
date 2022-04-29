# 스택이 꼭 리스트일 필요가 있을까?
# 문자열 문제는 앞뒤로 붙이려면 그냥 +만 해주면 된다는 깨달음(?)을 얻음
# 공백 출력 방향 주의

import sys
input = sys.stdin.readline
string = list(map(str, input().rstrip()))

bracket = False
ans = ''
tmp = ''
for chr in string:
    if bracket == False:
        if chr == '<':
            bracket = True
            tmp = tmp + chr
        elif chr == ' ': # 태그 외부라고 하더라도 공백은 정방향으로 출력되어야 함
            tmp = tmp + chr
            ans += tmp
            tmp = ''
        else: # 태그 외부일 때는 문자열이 역방향으로 출력되어야함
            tmp = chr + tmp
    
    elif bracket == True:
        tmp = tmp + chr # 태그 내부일 때는 문자열이 정방향으로 출력되어야함
        if chr == '>':
            bracket = False
            ans += tmp
            tmp = ''

print(ans + tmp)