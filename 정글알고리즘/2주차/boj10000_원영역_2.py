import sys

N = int(sys.stdin.readline())

circles = []

for _ in range(N):
    circle = list(map(int, sys.stdin.readline().split()))
    circles.append((circle[0]-circle[1], '('))                 # 시작점
    circles.append((circle[0]+circle[1], ')'))                 # 끝점

circles.sort(key=lambda x:(x[0], -ord(x[1])))

stk = []
res = 1
for i in range(2*N):

    pos, bracket = circles[i]

    if not stk:
        info_dic = {'pos':pos, 'bracket':bracket, 'status':1}
        stk.append(info_dic)
        continue
    
    if bracket == '(':
        if stk[-1]['pos'] == pos:
            stk[-1]['status'] = 2
        info_dic = {'pos':pos, 'bracket':bracket, 'status':1}
        stk.append(info_dic)
    else:
        tmp = stk.pop()
        res += tmp['status']

        if i != 2*N-1 and pos != circles[i+1][0]:
            stk[-1]['status'] = 1

print(res)