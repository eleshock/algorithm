import sys
input = sys.stdin.readline
# st : 스택, ans : 정답배열
stk = []
ans = []
while True:
    total, *info = list(map(int, input().split()))
    if total == 0:
        break
    temp = []
    for i in range(len(info)):
        # cut: 새로 꺼낸 직사각형의 인덱스 저장
        cut = i
        # 스택이 비어있지 않고 top의 높이보다 새로운 직사각형의 높이가 더 작다면
        while stk and stk[-1][0] > info[i]:
            # 스택에서 높이와 인덱스를 pop
            h, idx = stk.pop()
            # 넓이 저장
            temp.append(h * (i - idx))
            # 왼쪽으로 확장가능한 인덱스를 pop한 직사각형으로부터 받아와 갱신
            cut = idx
        # 조건에 해당하지 않는 경우 튜플 형태로 스택에 넣어줌
        stk.append((info[i], cut))
    # for문 다 돌렸을 때 스택에 원소가 남아있으면 빼서 확인해주자
    while stk:
        h, idx = stk.pop()
        temp.append(h * (total - idx))
    ans.append(max(temp))

for i in ans:
    print(i)